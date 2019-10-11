process_timestamp = [
    (1,5),
    (2,2),
    (3,12)
]

def wound_wait():
    current_p_t = process_timestamp[0]
    print("Process",current_p_t[0]," has a lock on resource")
    for i in range(1,len(process_timestamp)):
        p_t = process_timestamp[i]
        print("Process",p_t[0]," requesting for lock")
        if p_t[1] < current_p_t[1]:
            # Older process so give resource and rollback
            current_p_t = p_t
            print("Process",current_p_t[0]," has a lock on resource")
        else:
            # 
            print("Process",current_p_t[0]," has a lock on resource")
            print("Process",p_t[0],"waiting")

def wait_die():
    current_p_t = process_timestamp[0]
    print("Process",current_p_t[0]," has a lock on resource")
    for i in range(1,len(process_timestamp)):
        p_t = process_timestamp[i]
        print("Process",p_t[0]," requesting for lock")
        if p_t[1] < current_p_t[1]:
            # Older process so it can wait
            current_p_t = p_t
            print("Process",current_p_t[0]," has a lock on resource")
            print("Process",p_t[0],"waiting")
        else:
            # Younger process which is killed
            print("Process",current_p_t[0]," has a lock on resource")
            print("Process",p_t[0],"killed")


def main():
    print("Wound - Wait")
    wound_wait()
    print("-"*50)
    print("Wait - Die")
    wait_die()

if __name__ == "__main__":
    main()