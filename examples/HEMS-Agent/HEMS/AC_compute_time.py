def AC_compute_time(A, B, C, T_out, Q_i, Q_s, Q_h, T_0, T_1, mdt, ddt):
    temp = T_0
    for i in range(1,mdt / ddt):  # mdt is the time clearance for the market @5min (300sec or 0.0833hrs) and ddt is the time clearance for the device @0.5min (30sec or 0.0083hrs)
        temp = A * temp + B * T_out + C * Q_h + C * (0.5 * Q_i + 0.5 * Q_s)
        if Q_h == 0:
            if (temp > T_1):
                break
        else:
            if (temp < T_1):
                break
    time = i * ddt
    return time