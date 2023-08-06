#!/usr/bin/env python3

"""Old losses that is converted for mmsegmentation

FIXME: update the losses so that we can reuse them
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

from ..builder import LOSSES


@LOSSES.register_module()
class BinaryEdgeLoss(nn.Module):
    def __init__(
        self,
        loss_weight=1.0,
        loss_name="loss_binary_edge",
    ):
        super().__init__()
        self.loss_weight = loss_weight
        self._loss_name = loss_name

    def forward(
        self,
        edge,  # logits
        edge_label,
        weight=None,
        ignore_index=255,
        **kwargs,
    ):
        log_p = edge.transpose(1, 2).transpose(2, 3).contiguous().view(1, -1)
        # NOTE: need to convert long to float
        target_t = (
            edge_label.transpose(1, 2).transpose(2, 3).contiguous().view(1, -1).float()
        )
        target_trans = target_t.clone()

        # remove ignore index?
        pos_index = target_t == 1
        neg_index = target_t == 0
        ignore_index = target_t > 1

        target_trans[pos_index] = 1
        target_trans[neg_index] = 0

        # pos_index = pos_index.data.cpu().numpy().astype(bool)
        # neg_index = neg_index.data.cpu().numpy().astype(bool)
        # ignore_index = ignore_index.data.cpu().numpy().astype(bool)

        weight = torch.Tensor(log_p.size()).fill_(0)
        pos_num = pos_index.sum()
        neg_num = neg_index.sum()
        sum_num = pos_num + neg_num
        weight[pos_index] = neg_num * 1.0 / sum_num
        weight[neg_index] = pos_num * 1.0 / sum_num

        weight[ignore_index] = 0

        weight = weight.to(edge.device)

        # FIXME: already applies sigmoid
        # https://github.com/nv-tlabs/GSCNN/issues/62
        # https://pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html#torch.nn.BCEWithLogitsLoss
        # "this loss combines a Sigmoid layer and the BCELoss in one single class."
        # FIXME: why isn't `target_trans` used?
        return self.loss_weight * F.binary_cross_entropy_with_logits(
            log_p,
            target_t,
            weight,
            reduction="mean",
        )

    @property
    def loss_name(self):
        return self._loss_name


@LOSSES.register_module()
class MultiLabelEdgeLoss(nn.Module):
    def __init__(
        self,
        loss_weight=1.0,
        loss_name="loss_multilabel_edge",
    ):
        super().__init__()
        self.loss_weight = loss_weight
        self._loss_name = loss_name

    def forward(
        self,
        edge,  # logits
        edge_label,
        weight=None,
        **kwargs,
    ):
        loss_total = 0

        # FIXME: could optimize for batched loss
        for i in range(edge_label.size(0)):  # iterate for batch size
            pred = edge[i]
            target = edge_label[i]

            num_pos = torch.sum(target)  # true positive number
            num_total = target.size(-1) * target.size(-2)  # true total number
            num_neg = num_total - num_pos
            pos_weight = (num_neg / num_pos).clamp(
                min=1, max=num_total
            )  # compute a pos_weight for each image

            max_val = (-pred).clamp(min=0)
            log_weight = 1 + (pos_weight - 1) * target
            loss = (
                pred
                - pred * target
                + log_weight
                * (max_val + ((-max_val).exp() + (-pred - max_val).exp()).log())
            )

            loss = loss.mean()
            loss_total = loss_total + loss

        loss_total = loss_total / edge_label.size(0)
        return self.loss_weight * loss_total

    @property
    def loss_name(self):
        return self._loss_name
