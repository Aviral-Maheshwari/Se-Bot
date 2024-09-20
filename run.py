from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
    #bot.change_currency(currency="Brazilian Real")
    bot.select_place_to_go("New Delhi")
    bot.selected_dates(check_in_date='2024-09-21',
                       check_out_date='2024-09-23')
    bot.select_adults(count=2)
    bot.searchButton()
    print("Exiting...")
    input("Hello")
