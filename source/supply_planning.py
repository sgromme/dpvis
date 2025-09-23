from functools import lru_cache
from math import inf


print("inf value is", inf)
print("type of inf is", type(inf))

def plan_lot_sizing_dp(
    demand,              # list[int]
    capacity,            # list[int], same length as demand
    F=200,               # setup cost if q>0
    c=10,                # variable production cost per unit
    h=1,                 # holding cost per unit carried to next period
    b=5,                 # backlog penalty per unit (negative inventory)
    inv0=0,              # initial inventory (can be negative)
    Imax=None,           # max positive inventory allowed in DP state
    Bmax=None            # max backlog allowed (positive number; state inv >= -Bmax)
) -> dict:
    """
    Returns:
      plan: dict with production q, inventory inv, backlog back, and total_cost
    """
    T = len(demand)
    assert len(capacity) == T

    # Reasonable bounds if not provided:
    total_demand = sum(demand)
    if Imax is None: Imax = total_demand          # generous upper bound
    if Bmax is None: Bmax = total_demand          # generous backlog bound

    # Clamp helper to keep states finite
    def feasible_inv(x):
        return (-Bmax <= x <= Imax)

    @lru_cache(None)
    def V(t, inv):
        # Out-of-bounds states are disallowed
        if not feasible_inv(inv):
            return inf

        if t == T:
            # Penalize remaining inventory/backlog at horizon end
            return h * max(inv, 0) + b * max(-inv, 0)

        best = inf
        # Enumerate production within capacity
        for q in range(0, capacity[t] + 1):
            inv_next = inv + q - demand[t]
            if not feasible_inv(inv_next):
                continue
            step_cost = (F if q > 0 else 0) + c * q \
                        + h * max(inv_next, 0) + b * max(-inv_next, 0)
            cand = step_cost + V(t + 1, inv_next)
            if cand < best:
                best = cand
        return best

    # Reconstruct decisions
    q = [0]*T
    inv = [0]*(T+1)
    inv[0] = inv0

    for t in range(T):
        best_q, best_val = 0, inf
        for prod in range(0, capacity[t] + 1):
            inv_next = inv[t] + prod - demand[t]
            if not feasible_inv(inv_next):
                continue
            step_cost = (F if prod > 0 else 0) + c * prod \
                        + h * max(inv_next, 0) + b * max(-inv_next, 0)
            cand = step_cost + V(t + 1, inv_next)
            if cand < best_val:
                best_val, best_q = cand, prod
        q[t] = best_q
        inv[t+1] = inv[t] + q[t] - demand[t]

    total_cost = V(0, inv0)
    backlog = [max(-x, 0) for x in inv]  # convenience view

    return {
        "q": q,
        "inventory": inv,
        "backlog": backlog,
        "total_cost": total_cost
    }

if __name__ == "__main__":
    # Example usage generate in VSC with GPT-4.1
    # demand = [20, 30, 10, 50]
    # capacity = [40, 40, 40, 40]
    # plan = plan_lot_sizing_dp(demand, capacity)
    # print("Production plan:", plan["q"])
    # print("Inventory levels:", plan["inventory"])
    # print("Backlog levels:", plan["backlog"])
    # print("Total cost:", plan["total_cost"])

    demand   = [12, 5, 0, 9, 7, 10]   # units needed each week
    capacity = [10,10,10,10,10,10]    # plant weekly capacity
    F=150
    c=8
    h=1
    b=100
    inv0=0
    plan = plan_lot_sizing_dp(demand, capacity, F, c, h, b, inv0)
    print("Lot Sizing Problem")
    print("Initial Inventory:", inv0)
    print("Demand:", demand)
    print("Production:",plan["q"])          # production by week
    print("Inventory", plan["inventory"])  # end-of-week inventory (negative = backlog)
    print("Backlog", plan["backlog"])    # end-of-week backlog
    print("Total Cost:", plan["total_cost"])
    
