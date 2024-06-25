def main():
    avg_miles = 0
    avg_gallons = 0
    count = 0

    while True:
        try:
            # input gallons
            gallons = float(input("Enter the gallons used (-1 to end): "))
            if gallons == -1:
                break

            # input miles
            miles = float(input("Enter the miles driven : "))
            
            # average 
            avg = miles / gallons
            print(f"the miles/gallon for this tank was: {avg:.6f}")
            
            avg_miles += miles
            avg_gallons += gallons
            count += 1

        except ValueError:
            print("try again")

    # count
    if count > 0:
        overall_avg = avg_miles / avg_gallons
        print(f"The overall average miles/gallon was: {overall_avg:.6f}")
    else:
        print("no data.")

if __name__ == "__main__":
    main()
