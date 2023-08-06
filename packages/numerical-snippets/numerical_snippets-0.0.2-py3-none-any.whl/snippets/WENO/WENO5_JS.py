"""WENO-JS

Ref: Jiang, Guang-Shan, and Chi-Wang Shu. "Efficient implementation of 
weighted ENO schemes." Journal of computational physics 126.1 (1996): 202-228.
"""


def WENO5_JS_L(vmm,vm,vo,vp,vpp):
    """WENO5_JS_L Reconstruction of the :math:`u_{i-1/2}^+` by WENO5-JS
    ::
        
                |___________S0__________|
                |                       |
                |       |___________S1__________|
                |       |                       |
                |       |       |___________S2__________|
              ..|---o---|---o---|---o---|---o---|---o---|...
                | I{i-2}| I{i-1}|  I{i} | I{i+1}| I{i+2}|
                                |+
                                i-1/2
        

    Args:
        vmm : :math:`u_{i-2}`
        vm : :math:`u_{i-1}` 
        vo : :math:`u_i`
        vp : :math:`u_{i+1}`
        vpp : :math:`u_{i+2}`
    Returns:
        :math:`u_{i-1/2}^+`
    """
    # Smooth Indicators (Beta factors)
    B0 = 13 / 12 * (vmm - 2 * vm + vo) ** 2 + 1 / 4 * (vmm - 4 * vm + 3 * vo) ** 2
    B1 = 13 / 12 * (vm - 2 * vo + vp) ** 2 + 1 / 4 * (vm - vp) ** 2
    B2 = 13 / 12 * (vo - 2 * vp + vpp) ** 2 + 1 / 4 * (3 * vo - 4 * vp + vpp) ** 2

    # Constants
    d0p = 3 / 10
    d1p = 6 / 10
    d2p = 1 / 10
    epsilon = 1e-6

    # Alpha weights
    alpha0p = d0p / (epsilon + B0) ** 2
    alpha1p = d1p / (epsilon + B1) ** 2
    alpha2p = d2p / (epsilon + B2) ** 2
    alphasump = alpha0p + alpha1p + alpha2p

    # ENO stencils weigths
    w0p = alpha0p / alphasump
    w1p = alpha1p / alphasump
    w2p = alpha2p / alphasump

    # Numerical Flux at cell boundary, $u_{i+1/2}^{+}$;
    fluxL = (
        w0p * (-vmm + 5 * vm + 2 * vo) / 6
        + w1p * (2 * vm + 5 * vo - vp) / 6
        + w2p * (11 * vo - 7 * vp + 2 * vpp) / 6
    )

    return fluxL

def WENO5_JS_R(vmm,vm,vo,vp,vpp):
    """WENO5_JS_L Reconstruction of the :math:`u_{i+1/2}^-` by WENO5-JS
    ::
        
                |___________S0__________|
                |                       |
                |       |___________S1__________|
                |       |                       |
                |       |       |___________S2__________|
              ..|---o---|---o---|---o---|---o---|---o---|...
                | I{i-2}| I{i-1}|  I{i} | I{i+1}| I{i+2}|
                                       -|
                                      i+1/2
        

    Args:
        vmm : :math:`u_{i-2}`
        vm : :math:`u_{i-1}` 
        vo : :math:`u_i`
        vp : :math:`u_{i+1}`
        vpp : :math:`u_{i+2}`
    Returns:
        :math:`u_{i+1/2}^-`
    """

    # Smooth Indicators (Beta factors)
    B0 = 13 / 12 * (vmm - 2 * vm + vo) ** 2 + 1 / 4 * (vmm - 4 * vm + 3 * vo) ** 2
    B1 = 13 / 12 * (vm - 2 * vo + vp) ** 2 + 1 / 4 * (vm - vp) ** 2
    B2 = 13 / 12 * (vo - 2 * vp + vpp) ** 2 + 1 / 4 * (3 * vo - 4 * vp + vpp) ** 2

    d0n = 1 / 10
    d1n = 6 / 10
    d2n = 3 / 10
    epsilon = 1e-6

    # Alpha weights
    alpha0n = d0n / (epsilon + B0) ** 2
    alpha1n = d1n / (epsilon + B1) ** 2
    alpha2n = d2n / (epsilon + B2) ** 2
    alphasumn = alpha0n + alpha1n + alpha2n

    # ENO stencils weigths
    w0n = alpha0n / alphasumn
    w1n = alpha1n / alphasumn
    w2n = alpha2n / alphasumn

    fluxR = (
        w0n * (2 * vmm - 7 * vm + 11 * vo) / 6
        + w1n * (-vm + 5 * vo + 2 * vp) / 6
        + w2n * (2 * vo + 5 * vp - vpp) / 6
    )
   
    return fluxR