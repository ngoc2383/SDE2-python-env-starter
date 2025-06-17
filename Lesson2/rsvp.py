#import party people file as a nickname
import partyguests as pg

#store imported lists as variables
guest_list = pg.guest_list
rsvp_list = pg.rsvp_list
#ask the user for their name
username = input("Your name: ").lower()

#check if their name is on the guest list
if username in guest_list:
  #if true, check if their name isn't already on the RSVP list
  if username not in rsvp_list:
    #if true, add their name to the RSVP list 
    rsvp_list.append(username)
    print('You has been added to the RSVP list')
    #otherwise, print a message that they've already RSVPd
  else:
    print('Already RSVP')
#if the name isn't on the guest list, ask the user how they know you 
else:
  print('How do I know you?? :O')
