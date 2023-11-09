import random
def algorint(bounds:list,seed=0):
    if len(bounds)!= 2: return 0 
    [MIN,MAX],I64=[bounds,9223372036854775807]
    RND=random.randint(0,I64) if not seed else int(seed)
    return [MIN+int((MAX-MIN)*(RND^2)/I64),hex(RND)]
def algorfloat(bounds:list,seed=0):
    if len(bounds)!= 2: return 0 
    [MIN,MAX],I64=[bounds,9223372036854775807]
    RND=random.randint(0,I64) if not seed else int(seed)
    return [MIN+((MAX-MIN)*(RND^2)/I64),hex(RND)]