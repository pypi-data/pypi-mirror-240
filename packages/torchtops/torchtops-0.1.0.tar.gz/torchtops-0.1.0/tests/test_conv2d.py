import torch
import torch.nn as nn
import torchtops


class TestUtils:
    def test_conv2d_no_bias(self):
        n, in_c, ih, iw = 1, 3, 32, 32  # torch.randint(1, 10, (4,)).tolist()
        out_c, kh, kw = 12, 5, 5
        s, p, d, g = 1, 1, 1, 1

        net = nn.Conv2d(
            in_c,
            out_c,
            kernel_size=(kh, kw),
            stride=s,
            padding=p,
            dilation=d,
            groups=g,
            bias=False,
        )
        data = torch.randn(n, in_c, ih, iw)
        out = net(data)

        _, _, oh, ow = out.shape

        res = torchtops.profile(net, inputs=(data,))
        flops = res["total_flops"]
        print(flops)
        assert flops == 810000, f"{flops} v.s. {810000}"
