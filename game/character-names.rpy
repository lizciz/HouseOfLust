
# Define character names and relations
# Characters are defined by a single letter, based on their default names/roles:
# m = mom
# b = big sister
# l = little sister
# p = player

init python:

    m_n = "Melinda"
    m_ns = "Melinda's"
    b_n = "Jolie"
    b_ns = "Jolie's"
    l_n = "Amanda"
    l_ns = "Amanda's"
    p_n = "Stephen"
    p_ns = "Stephen's"

    # Mom, Melinda
    m_r_l = "mother"
    m_r_b = "mother"
    m_r_p = "mother"
    m_nn_l = l_n
    m_nn_ls = l_ns
    m_nn_b = b_n
    m_nn_bs = b_ns
    m_nn_p = p_n
    m_nn_ps = p_ns
    m_ln = "Bennet"

    # Big sister, Jolie
    b_r_m = "daughter"
    b_r_l = "sister"
    b_r_p = "sister"
    b_nn_m = "mom"
    b_nn_ms = "mom's"
    b_nn_l = l_n
    b_nn_ls = l_ns
    b_nn_p = p_n
    b_nn_ps = p_ns
    b_ln = "Bennet"

    # Little sister, Amanda
    l_r_m = "daughter"
    l_r_b = "sister"
    l_r_p = "sister"
    l_r_ps = "sister's"
    l_nn_m = "mom"
    l_nn_ms = "mom's"
    l_nn_b = b_n
    l_nn_bs = b_ns
    l_nn_p = p_n
    l_nn_ps = p_ns
    l_ln = "Bennet"

    # Player
    p_r_m = "son"
    p_r_b = "brother"
    p_r_l = "brother"
    p_nn_m = "mom"
    p_nn_ms = "mom's"
    p_nn_b = b_n
    p_nn_bs = b_ns
    p_nn_l = l_n
    p_nn_ls = l_ns
    p_ln = "Bennet"

    # Some additional rules that need special handling
    # Players relation to both b and l, as in "b and l are my <insert label>"
    p_r_bl = "sisters"
    # Player refering to both b and l in 1st person, as in "i should talk to <insert label>"
    p1_ref_bl = "my sisters" # otherwise, e.g. "[r_nn_b!c] and [p_nn_l!c]"
    # Other character (when talking to player) refering to both b and l in 3rd person, as in "go and talk to <insert label>"
    p3_ref_bl = "your sisters" # otherwise, e.g. "[b_n!c] and [l_n!c]"