guest_list = ['ian', 'jonas', 'brandie']
space = '\n'

message0=(f"{guest_list[0].title()}, you are hereby invited to the grand family"\
" party of 2020!  Can't wait to see you there!")
message1=(f"{guest_list[1].title()}, you are hereby invited to the grand family"\
" party of 2020!  Can't wait to see you there!")
message2=(f"{guest_list[2].title()}, you are hereby invited to the grand family"\
" party of 2020!  Can't wait to see you there!")

print(message0)
print(message1)
print(message2)

guest_list_popped = guest_list.pop(1)
print(f"\n\t{guest_list_popped.title()} can't make it, and has been removed"\
" from the list.")
guest_list.insert(1, "sunny")

message0=(f"{guest_list[0].title()}, you are hereby invited to the grand family"\
" party of 2020!  Can't wait to see you there!")
message1=(f"{guest_list[1].title()}, you are hereby invited to the grand family"\
" party of 2020!  Can't wait to see you there!")
message2=(f"{guest_list[2].title()}, you are hereby invited to the grand family"\
" party of 2020!  Can't wait to see you there!")

print(space)
print(message0)
print(message1)
print(message2)

for guest_lista in guest_list:
    print(f"\n{guest_lista.title()}, we found a bigger venue at the Blackhawk"\
    " hotel for Aug 28th!")

guest_list.insert(0, 'emma')
guest_list.insert(3, 'weston')
guest_list.append('amy')

for guest_lista in guest_list:
    print(f"\nUPDATED INVITES!!!  {guest_lista.title()}, you are hereby"\
    " invited to the grand family party of 2020!  Can't wait to see you there!")

print(space)
message_no_table = "Hello all!  Sorry to say that the table won't be here in"\
" time for the party so we can only invite two people."
message_no_table_popped = f"{guest_list_popped.title()}, thanks for saying"\
" you'd come, but we won't have room unfortuantly.  Maybe next time!"
print(message_no_table)

print(space)
guest_list_popped = guest_list.pop()
print(guest_list)
print(f"{guest_list_popped.title()} Removed from list")
message_no_table_popped = f"{guest_list_popped.title()}, thanks for saying"\
" you'd come, but we won't have room unfortuantly.  Maybe next time!"
print(message_no_table_popped)

print(space)
guest_list_popped = guest_list.pop()
print(guest_list)
print(f"{guest_list_popped.title()} Removed from list")
message_no_table_popped = f"{guest_list_popped.title()}, thanks for saying"\
" you'd come, but we won't have room unfortuantly.  Maybe next time!"
print(message_no_table_popped)

print(space)
guest_list_popped = guest_list.pop()
print(guest_list)
print(f"{guest_list_popped.title()} Removed from list")
message_no_table_popped = f"{guest_list_popped.title()}, thanks for saying"\
" you'd come, but we won't have room unfortuantly.  Maybe next time!"
print(message_no_table_popped)

print(space)
guest_list_popped = guest_list.pop()
print(guest_list)
print(f"{guest_list_popped.title()} Removed from list")
message_no_table_popped = f"{guest_list_popped.title()}, thanks for saying "\
"you'd come, but we won't have room unfortuantly.  Maybe next time!"
print(message_no_table_popped)

print(space)
del guest_list[0]

del guest_list[0]

print(guest_list)
