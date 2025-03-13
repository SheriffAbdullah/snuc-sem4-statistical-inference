import math
import pandas as pd


def RejectHypothesis(test):
    print("\n*** Conclusion ***")
    print(f"Calculated '{test}' value lies in Rejection Region.")
    print("Conclusion: Reject 'H0', Accept 'H1'.")
    
    
def AcceptHypothesis(test):
    print("\n*** Conclusion ***")
    print(f"Calculated '{test}' value lies in Acceptance Region.")
    print("Conclusion: Accept 'H0'.")
    

def CalculateMean(vals):
    mean = sum(vals) / len(vals)
    return mean


def CalculateStandardDeviation(vals):
    mean = CalculateMean(vals)
    
    tmp = 0
    for val in vals:
        tmp += val ** 2
        
    tmp /= len(vals)
    variance = tmp - mean ** 2
    
    return math.sqrt(variance)


def tValue(los_percentage, df, tail):
    tTable_twoTailed = pd.DataFrame()
    tTable_oneTailed = pd.DataFrame()

    tTable_twoTailed['0.2'] = [3.078, 1.886, 1.638, 1.533, 1.476, 1.440, 1.415, 1.397, 1.383, 1.372, 1.363, 1.356, 1.350, 1.345, 1.341, 1.337, 1.333, 1.330, 1.328, 1.325, 1.323, 1.321, 1.319, 1.318, 1.316, 1.315, 1.314, 1.313, 1.311, 1.282]
    tTable_twoTailed['0.10'] = [6.314, 2.920, 2.353, 2.132, 2.015, 1.943, 1.895, 1.860, 1.833, 1.812, 1.796, 1.782, 1.771, 1.761, 1.753, 1.746, 1.740, 1.734, 1.729, 1.725, 1.721, 1.717, 1.714, 1.711, 1.708, 1.706, 1.703, 1.701, 1.699, 1.645]
    tTable_twoTailed['0.05'] = [12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.160, 2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086, 2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052, 2.048, 2.045, 1.960]
    tTable_twoTailed['0.02'] = [31.821, 6.965, 4.541, 3.747, 3.365, 3.143, 2.998, 2.896, 2.821, 2.764, 2.718, 2.681, 2.650, 2.624, 2.602, 2.583, 2.567, 2.552, 2.539, 2.528, 2.518, 2.508, 2.500, 2.492, 2.485, 2.479, 2.473, 2.467, 2.462, 2.326]
    tTable_twoTailed['0.01'] = [63.657, 9.925, 5.841, 4.604, 4.032, 3.707, 3.499, 3.355, 3.250, 3.169, 3.106, 3.055, 3.012, 2.977, 2.947, 2.921, 2.898, 2.878, 2.861, 2.845, 2.831, 2.819, 2.807, 2.797, 2.787, 2.779, 2.771, 2.763, 2.756, 2.576]
    tTable_twoTailed['0.001'] = [636.619, 31.598, 12.941, 8.610, 6.859, 5.959, 5.405, 5.041, 4.781, 4.587, 4.437, 4.318, 4.221, 4.140, 4.073, 4.015, 3.965, 3.922, 3.883, 3.850, 3.819, 3.792, 3.767, 3.745, 3.725, 3.707, 3.690, 3.674, 3.659, 3.291]
    
    # REMEMBER to use 'df.copy()', or else changes will be made to original DataFrame
    tTable_oneTailed = tTable_twoTailed.copy()
    tTable_oneTailed.columns = ['0.10', '0.05', '0.25', '0.01', '0.005', '0.0005']
    
    idx = (los_percentage) / 100
    
    if tail == 'two':
        return tTable_twoTailed[str(idx)][df-1]
    elif tail == 'left' or tail == 'right':
        return tTable_oneTailed[str(idx)][df-1]
    

def FValue(los_percentage, df1, df2):
    fTable_1 = pd.DataFrame()
    fTable_1['idx'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,40,60,120]
    fTable_1['1'] = [4052.181,98.503,34.116,21.198,16.258,13.745,12.246,11.259,10.561,10.044,9.646,9.33,9.074,8.862,8.683,8.531,8.4,8.285,8.185,8.096,8.017,7.945,7.881,7.823,7.77,7.721,7.677,7.636,7.598,7.562,7.314,7.077,6.851]
    fTable_1['2'] = [4999.5,99.0,30.817,18.0,13.274,10.925,9.547,8.649,8.022,7.559,7.206,6.927,6.701,6.515,6.359,6.226,6.112,6.013,5.926,5.849,5.78,5.719,5.664,5.614,5.568,5.526,5.488,5.453,5.42,5.39,5.179,4.977,4.787]
    fTable_1['3'] = [5403.352,99.166,29.457,16.694,12.06,9.78,8.451,7.591,6.992,6.552,6.217,5.953,5.739,5.564,5.417,5.292,5.185,5.092,5.01,4.938,4.874,4.817,4.765,4.718,4.675,4.637,4.601,4.568,4.538,4.51,4.313,4.126,3.949]
    fTable_1['4'] = [5624.583,99.249,28.71,15.977,11.392,9.148,7.847,7.006,6.422,5.994,5.668,5.412,5.205,5.035,4.893,4.773,4.669,4.579,4.5,4.431,4.369,4.313,4.264,4.218,4.177,4.14,4.106,4.074,4.045,4.018,3.828,3.649,3.48]
    fTable_1['5'] = [5763.65,99.299,28.237,15.522,10.967,8.746,7.46,6.632,6.057,5.636,5.316,5.064,4.862,4.695,4.556,4.437,4.336,4.248,4.171,4.103,4.042,3.988,3.939,3.895,3.855,3.818,3.785,3.754,3.725,3.699,3.514,3.339,3.174]
    fTable_1['6'] = [5858.986,99.333,27.911,15.207,10.672,8.466,7.191,6.371,5.802,5.386,5.069,4.821,4.62,4.456,4.318,4.202,4.102,4.015,3.939,3.871,3.812,3.758,3.71,3.667,3.627,3.591,3.558,3.528,3.499,3.473,3.291,3.119,2.956]
    fTable_1['7'] = [5928.356,99.356,27.672,14.976,10.456,8.26,6.993,6.178,5.613,5.2,4.886,4.64,4.441,4.278,4.142,4.026,3.927,3.841,3.765,3.699,3.64,3.587,3.539,3.496,3.457,3.421,3.388,3.358,3.33,3.304,3.124,2.953,2.792]
    fTable_1['8'] = [5981.07,99.374,27.489,14.799,10.289,8.102,6.84,6.029,5.467,5.057,4.744,4.499,4.302,4.14,4.004,3.89,3.791,3.705,3.631,3.564,3.506,3.453,3.406,3.363,3.324,3.288,3.256,3.226,3.198,3.173,2.993,2.823,2.663]
    fTable_1['9'] = [6022.473,99.388,27.345,14.659,10.158,7.976,6.719,5.911,5.351,4.942,4.632,4.388,4.191,4.03,3.895,3.78,3.682,3.597,3.523,3.457,3.398,3.346,3.299,3.256,3.217,3.182,3.149,3.12,3.092,3.067,2.888,2.718,2.559]
    fTable_1['10'] = [6055.847,99.399,27.229,14.546,10.051,7.874,6.62,5.814,5.257,4.849,4.539,4.296,4.1,3.939,3.805,3.691,3.593,3.508,3.434,3.368,3.31,3.258,3.211,3.168,3.129,3.094,3.062,3.032,3.005,2.979,2.801,2.632,2.472]
    fTable_1['12'] = [6106.321,99.416,27.052,14.374,9.888,7.718,6.469,5.667,5.111,4.706,4.397,4.155,3.96,3.8,3.666,3.553,3.455,3.371,3.297,3.231,3.173,3.121,3.074,3.032,2.993,2.958,2.926,2.896,2.868,2.843,2.665,2.496,2.336]
    fTable_1['15'] = [6157.285,99.433,26.872,14.198,9.722,7.559,6.314,5.515,4.962,4.558,4.251,4.01,3.815,3.656,3.522,3.409,3.312,3.227,3.153,3.088,3.03,2.978,2.931,2.889,2.85,2.815,2.783,2.753,2.726,2.7,2.522,2.352,2.192]
    fTable_1['20'] = [6208.73,99.449,26.69,14.02,9.553,7.396,6.155,5.359,4.808,4.405,4.099,3.858,3.665,3.505,3.372,3.259,3.162,3.077,3.003,2.938,2.88,2.827,2.781,2.738,2.699,2.664,2.632,2.602,2.574,2.549,2.369,2.198,2.035]
    fTable_1['24'] = [6234.631,99.458,26.598,13.929,9.466,7.313,6.074,5.279,4.729,4.327,4.021,3.78,3.587,3.427,3.294,3.181,3.084,2.999,2.925,2.859,2.801,2.749,2.702,2.659,2.62,2.585,2.552,2.522,2.495,2.469,2.288,2.115,1.95]
    fTable_1['30'] = [6260.649,99.466,26.505,13.838,9.379,7.229,5.992,5.198,4.649,4.247,3.941,3.701,3.507,3.348,3.214,3.101,3.003,2.919,2.844,2.778,2.72,2.667,2.62,2.577,2.538,2.503,2.47,2.44,2.412,2.386,2.203,2.028,1.86]
    fTable_1['40'] = [6286.782,99.474,26.411,13.745,9.291,7.143,5.908,5.116,4.567,4.165,3.86,3.619,3.425,3.266,3.132,3.018,2.92,2.835,2.761,2.695,2.636,2.583,2.535,2.492,2.453,2.417,2.384,2.354,2.325,2.299,2.114,1.936,1.763]
    fTable_1['60'] = [6313.03,99.482,26.316,13.652,9.202,7.057,5.824,5.032,4.483,4.082,3.776,3.535,3.341,3.181,3.047,2.933,2.835,2.749,2.674,2.608,2.548,2.495,2.447,2.403,2.364,2.327,2.294,2.263,2.234,2.208,2.019,1.836,1.656]
    fTable_1['120'] = [6339.391,99.491,26.221,13.558,9.112,6.969,5.737,4.946,4.398,3.996,3.69,3.449,3.255,3.094,2.959,2.845,2.746,2.66,2.584,2.517,2.457,2.403,2.354,2.31,2.27,2.233,2.198,2.167,2.138,2.111,1.917,1.726,1.533]

    fTable_5 = pd.DataFrame()
    fTable_5['idx'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,40,60,120]
    fTable_5['1'] = [161.4476,18.5128,10.128,7.7086,6.6079,5.9874,5.5914,5.3177,5.1174,4.9646,4.8443,4.7472,4.6672,4.6001,4.5431,4.494,4.4513,4.4139,4.3807,4.3512,4.3248,4.3009,4.2793,4.2597,4.2417,4.2252,4.21,4.196,4.183,4.1709,4.0847,4.0012,3.9201]
    fTable_5['2'] = [199.5,19.0,9.5521,6.9443,5.7861,5.1433,4.7374,4.459,4.2565,4.1028,3.9823,3.8853,3.8056,3.7389,3.6823,3.6337,3.5915,3.5546,3.5219,3.4928,3.4668,3.4434,3.4221,3.4028,3.3852,3.369,3.3541,3.3404,3.3277,3.3158,3.2317,3.1504,3.0718]
    fTable_5['3'] = [215.7073,19.1643,9.2766,6.5914,5.4095,4.7571,4.3468,4.0662,3.8625,3.7083,3.5874,3.4903,3.4105,3.3439,3.2874,3.2389,3.1968,3.1599,3.1274,3.0984,3.0725,3.0491,3.028,3.0088,2.9912,2.9752,2.9604,2.9467,2.934,2.9223,2.8387,2.7581,2.6802]
    fTable_5['4'] = [224.5832,19.2468,9.1172,6.3882,5.1922,4.5337,4.1203,3.8379,3.6331,3.478,3.3567,3.2592,3.1791,3.1122,3.0556,3.0069,2.9647,2.9277,2.8951,2.8661,2.8401,2.8167,2.7955,2.7763,2.7587,2.7426,2.7278,2.7141,2.7014,2.6896,2.606,2.5252,2.4472]
    fTable_5['5'] = [230.1619,19.2964,9.0135,6.2561,5.0503,4.3874,3.9715,3.6875,3.4817,3.3258,3.2039,3.1059,3.0254,2.9582,2.9013,2.8524,2.81,2.7729,2.7401,2.7109,2.6848,2.6613,2.64,2.6207,2.603,2.5868,2.5719,2.5581,2.5454,2.5336,2.4495,2.3683,2.2899]
    fTable_5['6'] = [233.986,19.3295,8.9406,6.1631,4.9503,4.2839,3.866,3.5806,3.3738,3.2172,3.0946,2.9961,2.9153,2.8477,2.7905,2.7413,2.6987,2.6613,2.6283,2.599,2.5727,2.5491,2.5277,2.5082,2.4904,2.4741,2.4591,2.4453,2.4324,2.4205,2.3359,2.2541,2.175]
    fTable_5['7'] = [236.7684,19.3532,8.8867,6.0942,4.8759,4.2067,3.787,3.5005,3.2927,3.1355,3.0123,2.9134,2.8321,2.7642,2.7066,2.6572,2.6143,2.5767,2.5435,2.514,2.4876,2.4638,2.4422,2.4226,2.4047,2.3883,2.3732,2.3593,2.3463,2.3343,2.249,2.1665,2.0868]
    fTable_5['8'] = [238.8827,19.371,8.8452,6.041,4.8183,4.1468,3.7257,3.4381,3.2296,3.0717,2.948,2.8486,2.7669,2.6987,2.6408,2.5911,2.548,2.5102,2.4768,2.4471,2.4205,2.3965,2.3748,2.3551,2.3371,2.3205,2.3053,2.2913,2.2783,2.2662,2.1802,2.097,2.0164]
    fTable_5['9'] = [240.5433,19.3848,8.8123,5.9988,4.7725,4.099,3.6767,3.3881,3.1789,3.0204,2.8962,2.7964,2.7144,2.6458,2.5876,2.5377,2.4943,2.4563,2.4227,2.3928,2.366,2.3419,2.3201,2.3002,2.2821,2.2655,2.2501,2.236,2.2229,2.2107,2.124,2.0401,1.9588]
    fTable_5['10'] = [241.8817,19.3959,8.7855,5.9644,4.7351,4.06,3.6365,3.3472,3.1373,2.9782,2.8536,2.7534,2.671,2.6022,2.5437,2.4935,2.4499,2.4117,2.3779,2.3479,2.321,2.2967,2.2747,2.2547,2.2365,2.2197,2.2043,2.19,2.1768,2.1646,2.0772,1.9926,1.9105]
    fTable_5['12'] = [243.906,19.4125,8.7446,5.9117,4.6777,3.9999,3.5747,3.2839,3.0729,2.913,2.7876,2.6866,2.6037,2.5342,2.4753,2.4247,2.3807,2.3421,2.308,2.2776,2.2504,2.2258,2.2036,2.1834,2.1649,2.1479,2.1323,2.1179,2.1045,2.0921,2.0035,1.9174,1.8337]
    fTable_5['15'] = [245.9499,19.4291,8.7029,5.8578,4.6188,3.9381,3.5107,3.2184,3.0061,2.845,2.7186,2.6169,2.5331,2.463,2.4034,2.3522,2.3077,2.2686,2.2341,2.2033,2.1757,2.1508,2.1282,2.1077,2.0889,2.0716,2.0558,2.0411,2.0275,2.0148,1.9245,1.8364,1.7505]
    fTable_5['20'] = [248.0131,19.4458,8.6602,5.8025,4.5581,3.8742,3.4445,3.1503,2.9365,2.774,2.6464,2.5436,2.4589,2.3879,2.3275,2.2756,2.2304,2.1906,2.1555,2.1242,2.096,2.0707,2.0476,2.0267,2.0075,1.9898,1.9736,1.9586,1.9446,1.9317,1.8389,1.748,1.6587]
    fTable_5['24'] = [249.0518,19.4541,8.6385,5.7744,4.5272,3.8415,3.4105,3.1152,2.9005,2.7372,2.609,2.5055,2.4202,2.3487,2.2878,2.2354,2.1898,2.1497,2.1141,2.0825,2.054,2.0283,2.005,1.9838,1.9643,1.9464,1.9299,1.9147,1.9005,1.8874,1.7929,1.7001,1.6084]
    fTable_5['30'] = [250.0951,19.4624,8.6166,5.7459,4.4957,3.8082,3.3758,3.0794,2.8637,2.6996,2.5705,2.4663,2.3803,2.3082,2.2468,2.1938,2.1477,2.1071,2.0712,2.0391,2.0102,1.9842,1.9605,1.939,1.9192,1.901,1.8842,1.8687,1.8543,1.8409,1.7444,1.6491,1.5543]
    fTable_5['40'] = [251.1432,19.4707,8.5944,5.717,4.4638,3.7743,3.3404,3.0428,2.8259,2.6609,2.5309,2.4259,2.3392,2.2664,2.2043,2.1507,2.104,2.0629,2.0264,1.9938,1.9645,1.938,1.9139,1.892,1.8718,1.8533,1.8361,1.8203,1.8055,1.7918,1.6928,1.5943,1.4952]
    fTable_5['60'] = [252.1957,19.4791,8.572,5.6877,4.4314,3.7398,3.3043,3.0053,2.7872,2.6211,2.4901,2.3842,2.2966,2.2229,2.1601,2.1058,2.0584,2.0166,1.9795,1.9464,1.9165,1.8894,1.8648,1.8424,1.8217,1.8027,1.7851,1.7689,1.7537,1.7396,1.6373,1.5343,1.429]
    fTable_5['120'] = [253.2529,19.4874,8.5494,5.6581,4.3985,3.7047,3.2674,2.9669,2.7475,2.5801,2.448,2.341,2.2524,2.1778,2.1141,2.0589,2.0107,1.9681,1.9302,1.8963,1.8657,1.838,1.8128,1.7896,1.7684,1.7488,1.7306,1.7138,1.6981,1.6835,1.5766,1.4673,1.3519]
    
    if los_percentage == 1:
        for i in range(len(fTable_1)):
            if fTable_1.iloc[i, 0] == df2:
                return fTable_1.iloc[i, df1]
            
    elif los_percentage == 5:
        for i in range(len(fTable_5)):
            if fTable_5.iloc[i, 0] == df2:
                return fTable_5.iloc[i, df1]


def ChiSquaredValue(los_percentage, df):
    chiSquaredTable = pd.DataFrame()
    chiSquaredTable["df"] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,40,50,60,70,80,90,100]
    chiSquaredTable["0.05"] = [3.841,5.991,7.815,9.488,11.07,12.592,14.067,15.507,16.919,18.307,19.675,21.026,22.362,23.685,24.996,26.296,27.587,28.869,30.144,31.41,32.671,33.924,35.172,36.415,37.652,38.885,40.113,41.337,42.557,43.773,55.758,67.505,79.082,90.531,101.879,113.145,124.342]
    chiSquaredTable["0.01"] = [6.635,9.21,11.345,13.277,15.086,16.812,18.475,20.09,21.666,23.209,24.725,26.217,27.688,29.141,30.578,32.0,33.409,34.805,36.191,37.566,38.932,40.289,41.638,42.98,44.314,45.642,46.963,48.278,49.588,50.892,63.691,76.154,88.379,100.425,112.329,124.116,135.807]

    idx = (los_percentage) / 100
    
    return chiSquaredTable[str(idx)][df-1]


def Binomial(x, n, p):
    q = 1 - p
    combination = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    return combination * (p ** x) * (q ** (n - x))


def Poisson(x, lam):
    return math.exp(-lam) * (lam ** x) / math.factorial(x)

def LargeSampleSingleMeanTest(size, sample_mean, popu_std_dev, popu_mean, tail):
    # Print Input Data
    print("***** Test for Single Mean *****")
    print("*** Given Data ***")
    print(f"Sample Size = {size}")
    print(f"Sample Mean = {sample_mean}")
    print(f"Population Standard Deviation = {popu_std_dev}")
    print(f"Population Mean = {popu_mean}")
    print(f"It is a {tail}-tailed test.")
    
    # State the Hypotheses
    print("\nNull Hypothesis, H0: mean = popu_mean")
    
    if tail == 'two':
        print("Alternate Hypothesis, H1: mean != popu_mean")
    elif tail == 'left':
        print("Alternate Hypothesis, H1: mean < popu_mean")
    elif tail == 'right':
        print("Alternate Hypothesis, H1: mean > popu_mean")
    
    # Calculate the Test Statistic
    z_calc = (sample_mean - popu_mean) / (popu_std_dev / math.sqrt(size))
    print("\n*** Test Statistic ***")
    print(f"Z_calc = {z_calc}")
    
    los_percentage = [5, 1]
    z_alpha_twoTailed = [1.96, 2.58] # For Two-Tailed Tests
    z_alpha_oneTailed = [1.68, 2.33] # For One-Tailed Tests
    
    # Two-tailed Test
    if tail == 'two':
        # For both 5% and 1% LoS
        for i in range(2):
            print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, Z_alpha = {z_alpha_twoTailed[i]}")
            
            if abs(z_calc) > z_alpha_twoTailed[i]:
                RejectHypothesis('Z')
            else:
                AcceptHypothesis('Z')
        
    # One-tailed Test
    elif tail == 'left' or tail == 'right':
        # For both 5% and 1% LoS
        for i in range(2):
            if tail == 'left':
                print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, Z_alpha = {-z_alpha_oneTailed[i]}")
            elif tail == 'right':
                print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, Z_alpha = {z_alpha_oneTailed[i]}")
            
            if abs(z_calc) > z_alpha_oneTailed[i]:
                RejectHypothesis('Z')
            else:
                AcceptHypothesis('Z')
 

def LargeSampleTwoMeansTest(size1, mean1, std_dev1, size2, mean2, std_dev2, tail, same_popu=False):
    if same_popu == True:
        choice = input("Is there a value for population standard deviation? (y/n): ")
        if choice == 'y':
            popu_std_dev = float(input("Enter value: "))
    
    # Print Input Data
    print("\n***** Test for Two Sample Means *****")
    print("*** Given Data ***")
    print("Sample 1:")
    print(f"Size = {size1}")
    print(f"Mean = {mean1}")
    print(f"Standard Deviation = {std_dev1}")
    print("\nSample 2:")
    print(f"Size = {size2}")
    print(f"Mean = {mean2}")
    print(f"Standard Deviation = {std_dev2}")
    print()
    
    # If Samples are from 1 Population with SAME Standard Deviation
    if same_popu == True:
        # Calculate Population Standard Deviation using Sample Standard Deviations
        if choice == 'n':
            popu_var = (size1 * std_dev1 ** 2 + size2 * std_dev2 ** 2) / (size1 + size2)
            popu_std_dev = math.sqrt(popu_var)
        else:
            pass # Use given population standard deviation value
        
        print(f"Population Standard Deviation: {popu_std_dev}")
    
    print(f"It is a {tail}-tailed test.")
    
    # State the Hypotheses
    print("\nNull Hypothesis, H0: mean1 = mean2")
    
    if tail == 'two':
        print("Alternate Hypothesis, H1: mean1 != mean1")
    elif tail == 'left':
        print("Alternate Hypothesis, H1: mean1 < mean2")
    elif tail == 'right':
        print("Alternate Hypothesis, H1: mean1 > mean2")
    
    # Calculate the Test Statistic
    if same_popu == True:
        z_calc = (mean1 - mean2) / (popu_std_dev * math.sqrt( (1/size1) + (1/size2) ))
    else:
        z_calc = (mean1 - mean2) / math.sqrt( ((std_dev1 ** 2) / size1) + ((std_dev2 ** 2) / size2) )
        
    print("\n*** Test Statistic ***")
    print(f"Z_calc = {z_calc}")
    
    los_percentage = [5, 1]
    z_alpha_twoTailed = [1.96, 2.58] # For Two-Tailed Tests
    z_alpha_oneTailed = [1.68, 2.33] # For One-Tailed Tests
    
    # Two-tailed Test
    if tail == 'two':
        # For both 5% and 1% LoS
        for i in range(2):
            print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, Z_alpha = {z_alpha_twoTailed[i]}")
            
            if abs(z_calc) > z_alpha_twoTailed[i]:
                RejectHypothesis('Z')
            else:
                AcceptHypothesis('Z')
        
    # One-tailed Test
    elif tail == 'left' or tail == 'right':
        # For both 5% and 1% LoS
        for i in range(2):
            if tail == 'left':
                print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, Z_alpha = {-z_alpha_oneTailed[i]}")
            elif tail == 'right':
                print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, Z_alpha = {z_alpha_oneTailed[i]}")
            
            if abs(z_calc) > z_alpha_oneTailed[i]:
                RejectHypothesis('Z')
            else:
                AcceptHypothesis('Z')
                
def SmallSampleSingleMeanTest(size, vals, popu_mean, tail, vals_exist=False):
    if vals_exist == True:
        sample_mean = CalculateMean(vals)
        sample_std_dev = CalculateStandardDeviation(vals)
    else:
        sample_mean = float(input("Enter sample mean: "))
        sample_std_dev = float(input("Enter sample standard deviation: "))
        
    df = size - 1
    
    # Print Input Data
    print("***** Test for Single Mean *****")
    print("*** Given Data ***")
    print(f"Sample Size = {size}")
    print(f"Sample Mean = {sample_mean}")
    print(f"Sample Standard Deviation = {sample_std_dev}")
    print(f"Population Mean = {popu_mean}")
    print(f"Degrees of Freedom = {df}")
    print(f"\nIt is a {tail}-tailed test.")
    
    # State the Hypotheses
    print("\nNull Hypothesis, H0: mean = popu_mean")
    
    if tail == 'two':
        print("Alternate Hypothesis, H1: mean != popu_mean")
    elif tail == 'left':
        print("Alternate Hypothesis, H1: mean < popu_mean")
    elif tail == 'right':
        print("Alternate Hypothesis, H1: mean > popu_mean")
    
    # Calculate the Test Statistic
    t_calc = (sample_mean - popu_mean) / (sample_std_dev / math.sqrt(size - 1))
    print("\n*** Test Statistic ***")
    print(f"t_calc = {t_calc}")
    
    los_percentage = [5, 1]
    
    # Two-tailed Test
    if tail == 'two':
        # For both 5% and 1% LoS
        for i in range(2):
            t_alpha = tValue(los_percentage[i], df, tail)
            print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, t_alpha({df}) = {t_alpha}")
            
            if abs(t_calc) > t_alpha:
                RejectHypothesis('t')
            else:
                AcceptHypothesis('t')
        
        # Find Confidence Limits
        print("\n*** Confidence Limits ***")
        
        for i in range(2):
            t_alpha = tValue(los_percentage[i], df, tail)
            l_val = sample_mean - (t_alpha * sample_std_dev / math.sqrt(size - 1))
            r_val = sample_mean + (t_alpha * sample_std_dev / math.sqrt(size - 1))
            print(f"{100-los_percentage[i]}% Confidence Limits: [{l_val}, {r_val}]")
            
    # One-tailed Test
    elif tail == 'left' or tail == 'right':
        # For both 5% and 1% LoS
        for i in range(2):
            t_alpha = tValue(los_percentage[i], df, tail)
            
            if tail == 'left':
                print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, t_alpha({df}) = {-t_alpha}")
            elif tail == 'right':
                print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, t_alpha({df}) = {t_alpha}")
            
            if abs(t_calc) > t_alpha:
                RejectHypothesis('t')
            else:
                AcceptHypothesis('t')
                

def SmallSampleTwoMeansTest(size1, vals1, size2, vals2, tail, vals_exist=False):
    if vals_exist == True:
        mean1 = CalculateMean(vals1)
        mean2 = CalculateMean(vals2)
        std_dev1 = CalculateStandardDeviation(vals1)
        std_dev2 = CalculateStandardDeviation(vals2)
        
    else:
        print("Sample 1:")
        mean1 = float(input("Enter mean: "))
        std_dev1 = float(input("Enter standard deviation: "))
        
        print("Sample 2:")
        mean2 = float(input("Enter mean: "))
        std_dev2 = float(input("Enter standard deviation: "))
        
    df = size1 + size2 - 2
    
    # Print Input Data
    print("***** Test for Two Sample Means *****")
    print("*** Given Data ***")
    print("Sample 1:")
    print(f"Size = {size1}")
    print(f"Mean = {mean1}")
    print(f"Standard Deviation = {std_dev1}")
    print("\nSample 2:")
    print(f"Size = {size2}")
    print(f"Mean = {mean2}")
    print(f"Standard Deviation = {std_dev2}")
    print()
    
    # State the Hypotheses
    print("\nNull Hypothesis, H0: mean = popu_mean")
    
    if tail == 'two':
        print("Alternate Hypothesis, H1: mean != popu_mean")
    elif tail == 'left':
        print("Alternate Hypothesis, H1: mean < popu_mean")
    elif tail == 'right':
        print("Alternate Hypothesis, H1: mean > popu_mean")
    
    # Calculate the Test Statistic
    t_calc = (mean1 - mean2) / math.sqrt( (((size1 * std_dev1 ** 2) + (size2 * std_dev2 ** 2)) / (size1 + size2 - 2)) * ((1/size1) + (1/size2) ))
    print("\n*** Test Statistic ***")
    print(f"t_calc = {t_calc}")
    
    los_percentage = [5, 1]
    
    # Two-tailed Test
    if tail == 'two':
        # For both 5% and 1% LoS
        for i in range(2):
            t_alpha = tValue(los_percentage[i], df, tail)
            print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, t_alpha({df}) = {t_alpha}")
            
            if abs(t_calc) > t_alpha:
                RejectHypothesis('t')
            else:
                AcceptHypothesis('t')
            
    # One-tailed Test
    elif tail == 'left' or tail == 'right':
        # For both 5% and 1% LoS
        for i in range(2):
            t_alpha = tValue(los_percentage[i], df, tail)
            
            if tail == 'left':
                print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, t_alpha({df}) = {-t_alpha}")
            elif tail == 'right':
                print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, t_alpha({df}) = {t_alpha}")
            
            if abs(t_calc) > t_alpha:
                RejectHypothesis('t')
            else:
                AcceptHypothesis('t')
           

def PairedTTest(size, vals1, vals2, tail):
    vals = [i-j for i, j in zip(vals1, vals2)]
    mean = CalculateMean(vals)
    std_dev = CalculateStandardDeviation(vals)
    df = size -1
    
    # Print Input Data
    print("***** Test for Two Sample Means *****")
    print("*** Given Data ***")
    print(f"Size = {size}")
    print(f"Mean = {mean}")
    print(f"Standard Deviation = {std_dev}")
    print()
    
    # State the Hypotheses
    print("\nNull Hypothesis, H0: mean = popu_mean")
    
    if tail == 'two':
        print("Alternate Hypothesis, H1: mean != popu_mean")
    elif tail == 'left':
        print("Alternate Hypothesis, H1: mean < popu_mean")
    elif tail == 'right':
        print("Alternate Hypothesis, H1: mean > popu_mean")
    
    # Calculate the Test Statistic
    t_calc = (mean) / (std_dev / math.sqrt(size - 1))
    print("\n*** Test Statistic ***")
    print(f"t_calc = {t_calc}")
    
    los_percentage = [5, 1]
    
    # Two-tailed Test
    if tail == 'two':
        # For both 5% and 1% LoS
        for i in range(2):
            t_alpha = tValue(los_percentage[i], df, tail)
            print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, t_alpha({df}) = {t_alpha}")
            
            if abs(t_calc) > t_alpha:
                RejectHypothesis('t')
            else:
                AcceptHypothesis('t')
            
    # One-tailed Test
    elif tail == 'left' or tail == 'right':
        # For both 5% and 1% LoS
        for i in range(2):
            t_alpha = tValue(los_percentage[i], df, tail)
            
            if tail == 'left':
                print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, t_alpha = {-t_alpha}")
            elif tail == 'right':
                print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, t_alpha = {t_alpha}")
            
            if abs(t_calc) > t_alpha:
                RejectHypothesis('t')
            else:
                AcceptHypothesis('t')
          
             
def FTest(size1, vals1, size2, vals2, sssd_exists=False):
    if sssd_exists == True:
        sssd1 = float(input("Enter value for SSSD1: "))
        sssd2 = float(input("Enter value for SSSD2: "))
        
        # SSSD = Sum of the Squares of the Standard Deviations 
        # 'S' (Uppercase)
        std_dev1 = sssd1 / (size1 - 1)
        std_dev2 = sssd2 / (size2 - 1)
    else:
        mean1 = CalculateMean(vals1)
        sssd1 = sum([(x - mean1) ** 2 for x in vals1])
        
        mean2 = CalculateMean(vals2)
        sssd2 = sum([(x - mean2) ** 2 for x in vals2])
        
        # SSSD = Sum of the Squares of the Standard Deviations 
        # 's' (lowercase)
        std_dev1 = sssd1 / size1
        std_dev2 = sssd2 / size2
        
    
    
    # Sample with larger Standard Deviation will be on the Numerator
    if std_dev1 > std_dev2:
        num = 1
        
        # First Degree of Freedom must be of Numerator Sample
        df1 = size1 - 1
        df2 = size2 - 1
        
    else:
        num = 2
        
        # First Degree of Freedom must be of Denominator Sample
        df1 = size2 - 1
        df2 = size1 - 1
    
    print(df1, df2)
    
    
    # Print Input Data
    print("\n***** Test for Two Sample Means *****")
    print("*** Given Data ***")
    print("Sample 1:")
    print(f"Size = {size1}")
    print(f"Sum of Squares of Standard Deviation  = {sssd1}")
    print(f"Standard Deviation = {std_dev1}")
    print("\nSample 2:")
    print(f"Size = {size2}")
    print(f"Sum of Squares of Standard Deviation = {sssd2}")
    print(f"Standard Deviation = {std_dev2}")
    print()
    
    # State the Hypotheses
    print("\nNull Hypothesis, H0: mean1 = mean2")
    print("Alternate Hypothesis, H1: mean1 != mean1")
    
    
    # Calculate the Test Statistic
    if num == 1:  
        f_calc = std_dev1 / std_dev2
    elif num == 2:
        f_calc = std_dev2 / std_dev1
    
    print("\n*** Test Statistic ***")
    print(f"F_calc = {f_calc}")
    
    los_percentage = [5, 1]
    
    # For both 5% and 1% LoS
    for i in range(2):
        f_alpha = FValue(los_percentage[i], df1, df2)
        print(f"\nAt {los_percentage[i]}% LoS: \nCritical Value, F_alpha({df1}, {df2}) = {f_alpha}")
        
        if f_calc > f_alpha:
            RejectHypothesis('F')
        else:
            AcceptHypothesis('F')
        
 
def ChiSquaredGroupingCondition(expectedFreqs, groupingVal=5):
    for x in expectedFreqs:
        if x <= groupingVal:
            return True
        
    return False


def ChiSquaredGrouping(expectedFreqs, observedFreqs, groupingVal=5):
    while ChiSquaredGroupingCondition(expectedFreqs):
        expectedFreqs_final = []
        observedFreqs_final = []
        
        expectedFreqs.append(0)
        observedFreqs.append(0)
        
        i = 1
        while i < (len(expectedFreqs)):
            if expectedFreqs[i] <= 5 or expectedFreqs[i-1] <= 5:
                observedFreqs_final.append(observedFreqs[i-1] + observedFreqs[i])
                expectedFreqs_final.append(expectedFreqs[i-1] + expectedFreqs[i])
                i+=2
            else:
                observedFreqs_final.append(observedFreqs[i-1])
                expectedFreqs_final.append(expectedFreqs[i-1])
                i+=1
    
        # Print new grouped values
        # print(expectedFreqs)
        # print(expectedFreqs_final)
        # print(observedFreqs)
        # print(observedFreqs_final)
    
        expectedFreqs = expectedFreqs_final
        observedFreqs = observedFreqs_final
        
    return expectedFreqs, observedFreqs
    
    
def ChiSquaredTest(xVals, observedFreqs, distrib):
    # Assumption: xVals is in ascending order
    
    N = sum(observedFreqs)
    
    print(f"Sum of Observed Frequencies = {N}")
    print(f"Distribution = {distrib.title()}\n")
    
    if distrib == 'uniform':
        mean = sum(observedFreqs) / len(observedFreqs)
        
        print("Parameters for Uniform Distribution are 'mean'.")
        print(f"mean = {mean}")
        print()
        
        expectedFreqs = [mean for i in range(len(observedFreqs))]
        
    elif distrib == 'binomial':
        n = xVals[-1]
        
        # Mean of Distribution = np = sum(observedFreqs * x) / sum(observedFeqs)
        # Use this formula to find 'p'
        np = sum([freq * x for freq, x in zip(observedFreqs, xVals)]) / N
        p = np / n
        
        print("Parameters for Binomial Distribution are 'n' & 'p'.")
        print(f"n = {n}")
        print(f"p = {p}")
        print()
        
        expectedFreqs = [N * Binomial(x, n, p) for x in xVals]

            
    elif distrib == 'poisson':
        n = xVals[-1]
        
        # Mean of Distribution = Lambda = sum(observedFreqs * x) / sum(observedFeqs)
        # Use this formula to find 'p'
        lam = sum([freq * x for freq, x in zip(observedFreqs, xVals)]) / N
        
        print("Parameter for Poission Distribution is 'lambda'.")
        print(f"lambda = {lam}")
        print()
        
        expectedFreqs = [N * Poisson(x, lam) for x in xVals]
        
    elif distrib == 'normal':
        n = xVals[-1]
        
        # Mean of Distribution = Lambda = sum(observedFreqs * x) / sum(observedFeqs)
        # Use this formula to find 'p'
        lam = sum([freq * x for freq, x in zip(observedFreqs, xVals)]) / N
        
        print("Parameter for Poission Distribution is 'lambda'.")
        print(f"lambda = {lam}")
        print()
        
        expectedFreqs = [N * Poisson(x, lam) for x in xVals]
       
        
    expectedFreqs = [round(x) for x in expectedFreqs]
    
    # Display Expected Frequencies
    print("x \t\tOi \t\tEi")
    print("-" * 22)
    for i, j, k in zip(xVals, observedFreqs, expectedFreqs):
        print(f"{i} \t\t{j} \t\t{k}")
    
    print(f"\nsum(Observed Values) = {N}")
    print(f"sum(Expected Values) = {sum(expectedFreqs)}")
      
    expectedFreqs, observedFreqs = ChiSquaredGrouping(expectedFreqs, observedFreqs)
    diff = [o - e for o, e in zip(observedFreqs, expectedFreqs)]
    tmp = [(d ** 2) / e for d, e in zip(diff, expectedFreqs)]
    
    print("\n*** After Grouping ***\n")
    print("Oi \t\tEi \t\tOi - Ei\t\t(Oi - Ei)^2 / Ei")
    print("-" * 49)
    for i, j, k, l in zip(observedFreqs, expectedFreqs, diff, tmp):
        print(f"{i} \t\t{j} \t\t{k} \t\t\t{l}")
    
    tmp = [((o - e) ** 2) / e for o, e in zip(observedFreqs, expectedFreqs)]
    chiSquared_calc = sum(tmp)
    
    print(f"\nChi-Squared_calc = {chiSquared_calc}")
    
    if distrib == 'uniform':
        df = len(expectedFreqs) - 1
    else:
        df = len(expectedFreqs) - 2
        
    chiSquared_alpha = ChiSquaredValue(5, df)
    print(f"\nAt 5% LoS: \nCritical Value, Chi-Squared_alpha({df}) = {chiSquared_alpha}")
    
    if chiSquared_calc > chiSquared_alpha:
        RejectHypothesis('Chi-Squared')
    else:
        AcceptHypothesis('Chi-Squared')
    

def ChiSquaredTestForCorrellation():
    pass


#LargeSampleSingleMeanTest(900, 3.4, 2.61, 3.25, 'two')     
#LargeSampleTwoMeansTest(size1=1000, mean1=170, std_dev1=None, size2=2000, mean2=169, std_dev2=None, tail='two', same_popu=True)
#SmallSampleSingleMeanTest(size=22, vals=[], popu_mean=146.3, tail='right', vals_exist=False)
#SmallSampleTwoMeansTest(size1=10, vals1=[61, 63, 56, 63, 56, 63, 59, 56, 44, 61], size2=10, vals2=[55, 54, 47, 59, 51, 61, 57, 54, 64, 58], tail='two', vals_exist=True)
#PairedTTest(12, [50, 42, 51, 26, 35, 42, 60, 41, 70, 55, 62, 38], [62, 40, 61, 35, 30, 52, 68, 51, 84, 63, 72, 50], 'two')
#FTest(size1=9, vals1=[17, 27, 18, 25, 27, 29, 27, 23, 17], size2=8, vals2=[16, 16, 20, 16, 20, 17, 15, 21], sssd_exists=False)
#ChiSquaredTest(range(0, 6), [142, 156, 69, 27, 5, 1], 'poisson')
ChiSquaredTest([1, 2, 3, 4, 5, 6], [16, 20, 25, 14, 29, 28], 'uniform')
# Include Test for Proportionality.


#%%

'''
# Extracting Tables directly from HTML to Pandas
# Source: https://pbpython.com/pandas-html-table.html 

import pandas as pd
data = pd.read_html('http://www.socr.ucla.edu/Applets.dir/F_Table.html')

fTable_1 = data[4]
fTable_1 = fTable_1.drop('\\', axis=1)
fTable_1 = fTable_1.drop([5, 11, 17, 23, 29, 35])
fTable_1 = fTable_1.drop(39)
fTable_1 = fTable_1.drop('∞', axis=1)
tmp = list(range(1, 31))
tmp.extend([40, 60, 120])
fTable_1['idx'] = tmp
fTable_1['1'] = fTable_1['df1=1']
fTable_1 = fTable_1.drop('df1=1', axis=1)
cols = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
fTable_1 = fTable_1.iloc[:, cols]
fTable_1.T.to_csv('fTable_1.csv')

fTable_5 = data[10]
fTable_5 = fTable_5.drop('/', axis=1)
fTable_5 = fTable_5.drop([5, 11, 17, 23, 29, 35])
fTable_5 = fTable_5.drop(39)
fTable_5 = fTable_5.drop('∞', axis=1)
tmp = list(range(1, 31))
tmp.extend([40, 60, 120])
fTable_5['idx'] = tmp
fTable_5['1'] = fTable_5['df1=1']
fTable_5 = fTable_5.drop('df1=1', axis=1)
cols = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
fTable_5 = fTable_5.iloc[:, cols]
fTable_5.T.to_csv('fTable_5.csv')

data = pd.read_html('https://people.richland.edu/james/lecture/m170/tbl-chi.html')
chiSquared_table = data[0]
chiSquared_table = chiSquared_table[['df', '0.05', '0.01']]
chiSquared_table.T.to_csv('chiSquaredTable.csv')

'''
#%%


