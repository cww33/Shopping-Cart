# Shopping Cart Project

## Setup ##
### Repo Setup ###

Use the Github.com online interfacte to fork this repository into your own repository. You can name it as you wish but I would recomment naming it something simmilar to *Shopping_Cart*.

After creating the remote repo, use the Github.com online interface and click on the green button that says _Clone or Download_ and click on the option that says _Open in Desktop_. Once this is done you will be promted on your web browser asking if you want to open the repository on your Github desktop software, click on the option that says _Open GitHubDesktop.exe_. 

After you finish that, Navigate to the repo from the command line:

   ```
   cd ~/Desktop/shopping_cart
   ```
  

### Environment Setup ###

Create and Activate an Anaconda Virtual environment:

   ```
   conda create -n shopping_cart-env python=3.7 (first time only)
   conda activate shopping_cart-env
   ```
   
After that you will be able to run the Python script from the command-line:
   ```
   python shopping_cart.py
   ```


### Run the Program ###

Enter a number between 1 and 20 to select the item you want to put into your shopping cart.

Enter Done when finished selecting all your items.

The program will calculate the subtotal, tax total, and Total price and print out a receipt for you.

### Testing Program ###

To test the program enter:
 ```
pytest
``` 
and the program will ensure that the program behaves as it should. 