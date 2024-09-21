from booking.booking import Booking
#from booking.booking_filteration import BookingFilteration
with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.change_currency()
    bot.select_place_to_go("New Delhi")
    bot.selected_dates(check_in_date='2024-09-21',
                       check_out_date='2024-09-23')
    bot.select_adults(count=2)
    bot.searchButton()
    bot.apply_filterations(rating=3)
    print("Exiting...")
    input("Hello")
