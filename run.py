from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
    #bot.change_currency(currency="Brazilian Real")
    bot.select_place_to_go("New Delhi")
    print("Exiting...")
    input("Hello")
