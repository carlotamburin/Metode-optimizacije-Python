

def vrijemeLeta():
    let = []
    brojac = [0, 0, 0, 0, 0, 0, 0]
    time = input(
        "Unesite vrijeme polaska aviona u obliku dd:mm:gg:hh:mm:ss:zona ")
    time = time.split(":")
    # print(time)

    time2 = input(
        "Unesite vrijeme dolaska aviona u obliku dd:mm:gg:hh:mm:ss:zona ")
    time2 = time2.split(":")

    for i in range(0, len(time)):
        time[i] = int(time[i])
        time2[i] = int(time2[i])

        if(i == 0):
            if time[i] > time2[i]:
                let.append(time[i]-time2[i])
                let[i] = 30-let[i]
                brojac[i] = 1
            else:
                let.append(time2[i]-time[i])
            print(let[i])

        if(i == 1):
            if time[i] > time2[i]:
                let.append(time[i]-time2[i])
                let[i] = 12-let[i]
                brojac[i] = 1
            elif brojac[i-1] != 0:
                let.append(time2[i]-time[i]-1)
            else:
                let.append(time2[i]-time[i])
            print(let[i])

        if(i == 2):
            if time[i] <= time2[i]:
                if brojac[i-1] != 0:
                    let.append(time2[i]-time[i]-1)
                    print(let[i])
                    continue
                elif brojac[i-1] == 0:
                    let.append(time2[i]-time[i])
            else:
                print("Krivi unos godine")
                break
            print(let[i])

        if(i == 3):
            if time[i] > time2[i]:
                let.append(time[i]-time2[i])
                let[i] = 24-let[i]
                if let[0] > 0:
                    let[0] = let[0]-1
            else:
                let.append(time2[i]-time[i])
            print(let[i])

        if(i == 4):
            if time[i] > time2[i]:
                let.append(time[i]-time2[i])
                let[i] = 60-let[i]
                if let[3] > 0:
                    let[3] = let[3]-1
            else:
                let.append(time2[i]-time[i])
            print(let[i])

        if(i == 5):
            if time[i] > time2[i]:
                let.append(time[i]-time2[i])
                let[i] = 60-let[i]
                if let[4] > 0:
                    let[4] = let[4]-1
            else:
                let.append(time2[i]-time[i])
            print(let[i])

        if(i == 6):
            if(time[i] < 0 and time2[i] < 0):
                let.append(abs(time[i]-time2[i]))
                let[3] = let[3]+let[6]
            elif(time[i] < 0 or time2[i] < 0):
                let.append(abs(time[i])+abs(time2[i]))
                let[3] = let[3]+let[6]
                if let[3] > 24:
                    let[3] = let[3]-24
                    let[0] = let[0]+1

            elif time[i] > time2[i]:
                let.append(time[i]-time2[i])
                let[3] = let[3]+let[6]
                if let[3] > 24:
                    let[3] = let[3]-24
                    let[0] = let[0]+1

            else:
                let.append(time2[i]-time[i])
                let[3] = let[3]+let[6]
                if let[3] > 24:
                    let[3] = let[3]-24
                    let[0] = let[0]+1

            # print(let[i])
    print("\n")
    let.pop()
    print(let)


vrijemeLeta()
