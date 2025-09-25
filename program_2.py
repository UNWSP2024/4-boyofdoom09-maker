# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    total_tickets = 0 
while True: 
    movie_name = input('what movie do you want to watch? (type done to finish):')
    if movie_name.lower() == 'done': 
        break
    ticket_num = int(input(f"how many tickets for, {movie_name} "))
    total_tickets = total_tickets + ticket_num
print('you have,' , total_tickets, 'tickets')
    ######################


if __name__ == '__main__':
    main()
