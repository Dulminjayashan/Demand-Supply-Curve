import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d

print("\n")

# print the text with color and underline
print('           Demand & Supply Curve           ')




while True:
    
    print("\n")

    # Define the price, demand, and supply data as lists

    p = list(map(int, input("Enter prices : ").split()))
    d = list(map(int, input("Enter demands : ").split()))
    s = list(map(int, input("Enter supplies : ").split()))

    answer = input("Do you want to add new demand/supplies? (y/n)")
    if answer.lower() != "n":
                
            d1 = list(map(int, input("Enter New demands  : ").split()))
            s1 = list(map(int, input("Enter New supplies : ").split()))
            
            p_smooth = np.linspace(min(p), max(p), 2000)
            d_smooth = interp1d(p, d, kind='cubic')(p_smooth)
            s_smooth = interp1d(p, s, kind='cubic')(p_smooth)
            d1_smooth = interp1d(p, d1, kind='cubic')(p_smooth)
            s1_smooth = interp1d(p, s1, kind='cubic')(p_smooth)
             
            print("\n")

            data = {"Price": p, "Demand": d, "Supply": s, "Demand 1": d1, "Supply 2": s1}

            # Convert the dictionary to a pandas DataFrame
            df = pd.DataFrame(data)

            # Print the DataFrame
            print(df)

            # Create a demand and supply chart
            plt.plot(d_smooth, p_smooth, label="Demand",color='blue')
            plt.plot(s_smooth, p_smooth, label="Supply", color='red')
            plt.plot(d1_smooth, p_smooth, label="Demand 1", color='black')
            plt.plot(s1_smooth, p_smooth, label="Supply 2", color='brown')
            plt.ylabel("Price")
            plt.xlabel("Quantity")
            plt.title("Demand and Supply Chart")
            plt.grid(True, color='gray',linewidth=0.5, linestyle='--', which='both', alpha=0.5)

            print("\n")

            atol_range = np.linspace(0.1, 0.5, 1)
            for atol in atol_range:
                idx_array = np.argwhere(np.isclose(d1_smooth, s1_smooth, atol=atol)).flatten()
                if len(idx_array) > 0:
                    idx = idx_array[0]
                    neq_price = p_smooth[idx]
                    neq_quantity = d1_smooth[idx]        
                    print("New Equal Price",round(neq_price,1))
                    print("New Equal quantity",round(neq_quantity,1))

            atol_range = np.linspace(0.1, 0.5, 1)
            for atol in atol_range:
                idx_array = np.argwhere(np.isclose(d_smooth, s_smooth, atol=atol)).flatten()
                if len(idx_array) > 0:
                    idx = idx_array[0]
                    eq_price = p_smooth[idx]
                    eq_quantity = d_smooth[idx]
                    print("Equal Price",round(eq_price,1))
                    print("Equal quantity",round(eq_quantity,1))

            plt.plot(d_smooth, p_smooth, label=f"Equal Price={eq_price:.1f}",color='blue')
            plt.plot(s_smooth, p_smooth, label=f"Equal quantity={eq_quantity:.1f}", color='red')
            
            print("\n")
            
            plt.plot(d1_smooth, p_smooth, label=f" New Equal Price={neq_price:.1f}", color='black')
            plt.plot(s1_smooth, p_smooth, label=f" New Equal quantity={neq_quantity:.1f}", color='brown')

            plt.axhline(y=neq_price, color='black', linestyle='--')
            plt.axvline(x=neq_quantity, color='black', linestyle='--')
            plt.plot(neq_quantity, neq_price, marker='o', color='black')

            plt.axhline(y=eq_price, color='green', linestyle='--')
            plt.axvline(x=eq_quantity, color='green', linestyle='--')
            plt.plot(eq_quantity, eq_price, marker='o', color='green')

            print("\n")

            answer = input("Do you want to graph? (y/n)")
            if answer.lower() != "n":
                       
                plt.legend()
                plt.show()

                
                answer = input("Do you want to repeat the program? (y/n)")
                if answer.lower() != "y":
                    print("\n")
                    print("Thank You")
                    break

            elif answer.lower() != "y":
                        
                answer = input("Do you want to repeat the program? (y/n)")

                
            if answer.lower() != "y":
                     print("\n")
                     print("Thank You")
                     break

    elif answer.lower() != "y":       

                #p = [5, 10, 15, 20, 25]
                #d = [25, 20, 15, 10, 5]
                #d1= [20, 15, 10, 5, 0]
                #s = [5, 10, 15, 20, 25]
                #s1= [15, 20, 25, 30, 35]

                # Interpolate data to create smooth curves
                p_smooth = np.linspace(min(p), max(p), 2000)
                d_smooth = interp1d(p, d, kind='cubic')(p_smooth)
                s_smooth = interp1d(p, s, kind='cubic')(p_smooth)
                
                print("\n")

                # Create a dictionary to store the data
                data = {"Price": p, "Demand": d, "Supply": s}

                # Convert the dictionary to a pandas DataFrame
                df = pd.DataFrame(data)

                # Print the DataFrame
                print(df)

                # Create a demand and supply chart
                plt.plot(d_smooth, p_smooth, label="Demand",color='blue')
                plt.plot(s_smooth, p_smooth, label="Supply", color='red')
                plt.ylabel("Price")
                plt.xlabel("Quantity")
                plt.title("Demand and Supply Chart")
                plt.grid(True, color='gray',linewidth=0.5, linestyle='--', which='both', alpha=0.5)

                print("\n")

                # Find the intersection point of the demand and supply curves
                atol_range = np.linspace(0.1, 0.5, 1)
                for atol in atol_range:
                    idx_array = np.argwhere(np.isclose(d_smooth, s_smooth, atol=atol)).flatten()
                    if len(idx_array) > 0:
                        idx = idx_array[0]
                        eq_price = p_smooth[idx]
                        eq_quantity = d_smooth[idx]
                        print("Equal Price",round(eq_price))
                        print("Equal quantity",round(eq_quantity))
                        
                        print("\n")

                plt.plot(d_smooth, p_smooth, label=f"Equal Price= {eq_price:.1f}",color='blue')
                plt.plot(s_smooth, p_smooth, label=f"Equal quantity={eq_quantity:.1f}", color='red')
                        

                # Plot the intersection point with dashed lines
                plt.axhline(y=eq_price, color='green', linestyle='--')
                plt.axvline(x=eq_quantity, color='green', linestyle='--')
                plt.plot(eq_quantity, eq_price, marker='o', color='green')

                print("\n")

                answer = input("Do you want to graph? (y/n)")
                if answer.lower() != "n":

                    plt.legend()
                    plt.show()

                    answer = input("Do you want to repeat the program? (y/n)")
                    if answer.lower() != "y":
                        print("\n")
                        print("Thank You")
                        break
                    
                elif answer.lower() != "y":
    
                # Ask the user whether to repeat the program or not
                        answer = input("Do you want to repeat the program? (y/n)")

                # Check the user's answer and act accordingly
                if answer.lower() != "y":
                        print("\n")
                        print("Thank You")
                        break

        
        
        
