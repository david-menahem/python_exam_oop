from Lamp import Lamp
from enums.CustomerType import CustomerType
from enums.PaymentType import PaymentType
from model.Customer import Customer
from model.Item import Item
from model.RegularOrder import RegularOrder
from model.VipOrder import VipOrder

if __name__ == '__main__':
    item_one = Item(1,"Chess",40)
    item_two = Item(2,"Monopoly",50)
    item_three = Item(3,"Cards",10)
    item_four =Item (4,"Cup",5)
    customer_one = Customer(1,"David","Menahem","dvmena39@gmail.com","Rosh ha'ayin",CustomerType.REGULAR,30,[item_three],None)
    regular_order = RegularOrder(2,"Order_2",[item_one,item_two],customer_one,
                         PaymentType.CREDIT_CARD,"2024-05-15")
    items = customer_one.favorite_items
    customer_one.remove_from_favorites([item_one])
    for item in items:
        print(item.item_name)

    gift = Lamp()
    customer_one.take_gift(gift)
    if customer_one.gift:
        customer_one.gift.open_gift()





    # vip_order = VipOrder(1,"Order_1",[item_one,item_two],customer_one,
    #                      PaymentType.CREDIT_CARD,"2024-05-15")



