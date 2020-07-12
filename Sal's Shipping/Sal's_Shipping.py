def cost_of_ground_shipping(weight):
    flat_charge_fee = 20;
    cost_per_pound= 0;
    if weight>10 :
        cost_per_pound = 4.75;
    elif weight>6:
        cost_per_pound = 4.00;
    elif weight>2:
        cost_per_pound = 3.00;
    else:
        cost_per_pound = 1.50;
    return weight*cost_per_pound+flat_charge_fee;

def cost_of_drone_shipping(weight):
    flat_charge_fee = 0;
    cost_per_pound= 0;
    if weight>10 :
        cost_per_pound = 14.25;
    elif weight>6:
        cost_per_pound = 12.00;
    elif weight>2:
        cost_per_pound = 9.00;
    else:
        cost_per_pound = 4.50;
    return weight*cost_per_pound+flat_charge_fee;

def cheapest_dynamic_shipping_method(weight):
    drone_shipping_total = cost_of_drone_shipping(weight);
    ground_shipping_total = cost_of_ground_shipping(weight);
    if drone_shipping_total>ground_shipping_total:
        return "Ground", ground_shipping_total;
    elif ground_shipping_total>drone_shipping_total:
        return "Drone", drone_shipping_total;

def cheapest_flat_or_dynamic_method(weight):
    method,cost = cheapest_dynamic_shipping_method(weight);
    if cost>cost_of_premium_shipping:
        return "Premium", cost_of_premium_shipping;
    else:
        return method,cost;

def cheapest_shipping_method(weight):
    method, cost = cheapest_flat_or_dynamic_method(weight);
    print("The cheapest method of Shipping is : " + method);
    print("The total for " + method + " Shipping is : £" + str(cost));
    print("");

cost_of_premium_shipping = 125;

print(cost_of_ground_shipping(8.4));

print(cost_of_drone_shipping(1.5));

cheapest_shipping_method(4.8);
cheapest_shipping_method(41.5);