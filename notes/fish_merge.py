def merge(sea, fresh):
    result = []

    while not(not sea and not fresh):
        if(not sea):
            result += fresh
            break
        elif(not fresh):
            result += sea
            break

        if sea[0] < fresh[0]:
            fish = sea.pop(0)
        else:
            fish = fresh.pop(0)
        # print(fish, sea, fresh)
        result.append(fish)
    
    return result

def main():
    sea = ["Cod", "Herring", "Marlin"]
    fresh = ["Asp", "Carp", "Ide", "Trout"]

    result = merge(sea, fresh)
    # print(merge(sea=sea, fresh=fresh))
    print(result)

if __name__ == "__main__":
    main()