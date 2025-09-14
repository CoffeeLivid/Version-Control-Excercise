# This program pre-sells a limited number of cinema tickets (20 total).
# Each buyer can purchase up to 4 tickets. The program prompts for ticket
# requests, ensures validation, tracks the number of buyers, and ends when all
# tickets are sold.
# CONSTANT
MAX_TICKETS = 10
# Function to prompt the user for ticket input
def prompt_ticket_request(remaining_tickets):
 """Prompt user for the number of tickets and validate the input."""

 while True:
 try:
 print(f"There are {remaining_tickets} tickets remaining.")
 tickets = int(input("How many tickets would you like to purchase? (1 to
4): "))

 if tickets < 1 or tickets > 4:
 print("You can only purchase between 1 and 4 tickets.\n")
 elif tickets > remaining_tickets:
 print(f"Sorry, only {remaining_tickets} ticket(s) are left. Please
choose fewer tickets.\n")
 else:
 return tickets

 except ValueError:
 print("Invalid input. Please enter a whole number between 1 and 4.\n")
# Function to sell tickets
def sell_tickets():
 """Main function to control ticket sales and display results."""

 remaining_tickets = MAX_TICKETS
 total_buyers = 0
 while remaining_tickets > 0:
 requested_tickets = prompt_ticket_request(remaining_tickets)

 remaining_tickets -= requested_tickets
 total_buyers += 1

 print(f"You successfully purchased {requested_tickets} ticket(s).")
 print(f"Tickets remaining: {remaining_tickets}\n")
 print("All tickets have been sold.")
 print(f"Total number of buyers: {total_buyers}")
# Run the program

sell_tickets()
