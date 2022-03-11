Back to [README](../../README.md)

## **Contents**

- [**Automated Testing**](#automated-testing)
  - [**Bag**](#bag)
  - [**Checkout**](#checkout)
  - [**Profile**](#profile)
  - [**Products**](#products)
  - [**Blog**](#blog)
  - [**Home*](#home)
- [**Manual Testing**](#manual-testing)
  - [**Browsers**](#browsers)
  - [**Devices Used**](#devices-used)
  - [**Navigation**](#navigation)
  - [**Home Page**](#home-page)
  - [**Register Page**](#register-page)
  - [**Log In Page**](#log-in-page)
  - [**Profile Page**](#profile-page)
  - [**Products Pages**](#products-pages)
    - [**Products**](#products)
    - [**Product Details**](#product-details)
    - [**Add Product**](#add-product)
    - [**Edit Product**](#edit-product)
  - [**Bag**](#bag)
  - [**Checkout**](#checkout)
  - [**Blog Page**](#blog-page)
- [**User Stories Testing**](#user-stories-testing)
- [**Wave**](#wave)
- [**Lighthouse**](#lighthouse)
- [**Validators**](#validators)
  - [**HTML Validator**](#html-validator)
  - [**CSS Jigsaw**](#css-jigsaw)
  - [**JSHint**](#jshint)
  - [**PEP8**](#pep8])

### **Automated Testing**

#### **Bag**
Automated testing completed to:
- Test the calc_subtotal function works as expected
- Test the bag views work correctly
- Test the url works when loading the page
- Test the correct template loads on page load
- Test that the view_bag view works correctly
- Test that the add to bag view works as expected
- Test that the add_to_bag function adds the item to the bag
- Test that the add_to_bag view adds the product to the bag


#### **Checkout**
Automated testing of views was completed to:
- Test the checkout page loads correctly
- Test that the cache_checkout_data view works as expected
- Test the url works when loading the page
- Test the correct template loads on page load
- Test get checkout view when items in the bag

Automated testing of models was completed to:
- test the order model
- test order line model string method

Automated testing of forms was completed to:
- test to see if full name field is required
- test to see if email field is required
- test to see if phone number field is required
- test to see if country field is required
- test to see if town_or_city field is required
- test to see if street_address1 field is required

[Back to contents](#contents)

#### **Profiles**
Automated testing of views was completed to:
- Test the url works when loading the page
- Test the correct template loads on page load
- Test the profile page is accessible by name
- Test the profile form works if form is valid

Automated testing of models was completed to:
- Test retrieving the user profile

Automated testing of forms was completed to:
- Test that none of the form fields are required


#### **Products**
Automated testing of views was completed to:
- Test the url works when loading the page
- Test the correct template loads on page load
- Test products display
- Test that the search error message display correctly
- Test product detail page loads via name
- Test product detail page loads via template

Automated testing of models was completed to:
- Test category model string method
- Testing category models friendly name string method returns friendly name

Automated testing of forms was completed to:
- Test to see if name field is required
- Test to see if imagefield is required
- Test to see if Price field is required
- Test to see if description field is required


#### **Blog**
Automated testing of views was completed to:
- Test the blog page loads correctly
- Test the url works when loading the page
- Test the correct template loads on page load
- Test the blog page is accessible by name
- Test blog posts display as expected
- Test to see if the post string method returns the title as expected

Automated testing of forms was completed to:
- Test to see if name field is required
- Test to see if imagefield is required
- Test to see if Price field is required
- Test to see if description field is required

#### **Home**
Automated testing of views was completed to:
- Test the url works when loading the page
- Test the correct template loads on page load
- Test the home page is accessible by name

[Back to contents](#contents)

### **Manual Testing**
#### **Browsers**
The site was tested on:
- Google Chrome

#### **Devices Used**
The site was tested on these devices:
- iPhone 12
- Huawei P30 Lite
- Samsung 10
- iPhone 10
- Desktop
- Samsung A3


#### **Navigation**
    - all users

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Home button    | To redirect to home page | Click the home button | Button navigates to home | Pass |
| Navbar links | Clicking All Products takes user to All Products page | Click All Products | Redirected to All Products page | Pass |
|  | Clicking category takes user to the specific category page | Click each category in turn | Redirected to specific category page | Pass |
|   | Click Bag takes user to Bag page | Click Bag | Redirected to Bag page | Pass |
|   | Clicking Blog takes user to the Blog homepage | Click Blog | Redirected to Blog Page | Pass |
|   | Searching using Search Bar displays the product in the products page | Type Africa in search bar | Redirected to Products page with all African trips | Pass |


#### **Navigation**
    - users logged in
|  Navbar links   | Clicking Profile takes user to their profile page | Click Profile | Redirected to Profile Page | Pass |
|  | Click Log Out logs out the user | Click Log Out | User logged out and redirected to Log In | Pass |


    - user not logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Navbar links | Click Log In redirects to log in page | Click Log In | User redirected to Log In Page | Pass |
|  | Click Register redirects to log in page | Click Register | User redirected to Register Page | Pass |

[Back to contents](#contents)

#### **Home Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- |:----:|
| Floating menu | Clicking the arrow down button takes users further down the page to see shop options | Click arrow button | User redirected down the page to shopping options | Pass |
| Shopping Options | Clicking All trips, African trips, South American trips Links lead to different parts of shop | Click African trips, Sout American trips, Extra activities | Redirected to the relevant products in shop | Pass |
| Blog Card | Click to be taken to the blog for inspiration on holidays | Click link | User redirected to blog  | Pass |

#### **Register Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Register functionality | Form validation for email requires `@` symbol |  Attempt to register without `@` in input field | Form validation requests valid email address | Pass |
| | E-mail Again value must be same as Email value | Attempt to register with incorrect email in email again input field | Form validation requests email address must match | Pass |
| | Username must be between 4 and 15 characters | Attempt to enter username with less than 4 characters | Feedback error displayed | Pass |
| | Username must be between 4 and 15 characters | Attempt to enter username with more than 15 characters | Form restricts the user from using more than 15 characters | Pass |
| | Register with new user and password to be logged in and redirected to Profile page | Enter email address, name, username, password and click register | New account registered and profile page shown | Pass |

#### **Log In Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-----------------| ----------|  ---------- | :----: |
| Log in functionality | Correct user/pass combination directs user to their profile page with name displayed in tab | Log in with correct username/password combination | Redirected to user profile page with name displayed in tab | Pass |
|   | Incorrect username/password combination shows error message | Attempt to log in with incorrect credentials | "The username and/or password you specified are not correct." error message appears| Pass |
| Link to Register | Redirect to Register page | Click link to register | Redirected to Register page | Pass |

#### **Profile Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Personal Information | Personal information is visible if previously saved | Navigate to Profile page, view personal information | The personal information is visible in Personal Information section | Pass |
| | Personal information can be updated | Navigate to Profile page, change personal information, click update information. | The personal information is updated with the new details. | Pass |
| Order History | Order History is visible if order placed while logged in | Navigate to Profile page, view Order History Section | The Order History is visible | Pass |
| | Order information can be accessed by clicking order number | Navigate to Profile page, view Order History Section, click Order Number | Order Information is visible | Pass |

[Back to contents](#contents)

#### **Products Pages**

##### **Products**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| All products visible | Products page shows all products | Open Products page and view products | Pass |
|  | Searching by category shows products from that category | Select to search by each category | Products from each category successfully displayed | Pass |
| Back to top |When scrolled down the page a back to top arrow is presented for ease of motion through the website | Arrows is displayed in the bottom right and functional | Pass |

##### **Product Details**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Product Details | Product description displayed for individual product | Open Product Detail page and view products | Product details visible | Pass |
| Add to bag | Clicking Add To Bag adds the product to the bag | Open Product Detail page click add to bag | Product available in bag | Pass |
| Quantity | Adds and subtracts a number of products | Displays the quantity of products being purchased | Pass |

##### **Add Product**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Add Products | Only admin is allowed to visit add product page | Log in as non-superuser and attempt to access /products/add/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass |
| Form Validation | Required fields must be completed to add the product  | Attempt to add product without filling in a required field | Error message "Please fill in this field" | Pass |


##### **Edit Product**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Edit Products | Only admin is allowed to visit edit product page | Log in as non-superuser and attempt to access /products/<item_id>/edit/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass |
| Form Validation | Required fields must be completed to edit the product  | Attempt to edit product without filling in a required field | Error message "Please fill in this field" | Pass |

[Back to contents](#contents)

#### **Bag**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| View Items | Correct products are in the bag | Add product to bag and check quantity and total are in the bag | Expected products are in the bag | Pass |
| Update Items | Update the number of a product in the bag and it will reflect in bag and price | Change number of product in bag and check quantity and total has updated | Total and quantity updated | Pass |
| Remove Items | Click remove item for item to be removed from the bag | Click remove beside relevant product | Item removed from bag and notification to confirm this "Removed <item> from your bag" | Pass |

#### **Checkout**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| View Items | Correct products are in the checkout | Add products to bag, click Secure Checkout | Expected products are in the checkout product list | Pass |
| Form Validation | Required fields must be completed to complete  | Attempt to check out without filling in a required field | Error message "Please fill in this field" | Pass |


#### **Blog Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | ---- |
| All blog posts visible | Blog page shows all blog posts | Open Blog page and view posts | Posts visible | Pass |
| Add Post | Only logged in users are allowed to add posts | Log out and attempt to add blog post | User redirected to home page, error message displayed "Sorry, only users can do that." | Pass |


##### **Blog Post Detail**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Post Details | Post is displayed for individual slug | Open Post Detail page | Post visible | Pass |
| Comments | Add a comment form adds comment to post details page | While logged in navigate to post, fill out form, click add comment | Comment visible in post section | Pass |
|  | User must be logged in to add comment to post | While not logged in navigate to post, attempt to leave comment | Message revealed "Please log in to add a comment." | Pass |
| Edit Post | Only author of the post can edit a post | Log in as different user and attempt to edit blog post | Message displayed "You are not authorised to do this!" | Pass |
| Delete Post | Only author of the post can delete a post | Log in as different user and attempt to delete blog post | Message displayed "You are not authorised to do this!" | Pass |
| Comments | Add a comment form adds comment to post details page | While logged in navigate to post, fill out form, click add comment | Comment visible in post section | Pass |
|  | User must be logged in to add comment to post | While not logged in navigate to post, attempt to leave comment | Message revealed "Please log in to add a comment." | Pass |


[Back to contents](#contents)


### User Stories Testing

| # | As a/an     | I want to be able to...                    | So that I can...                            | Achieved on...                     |
|---|-------------|--------------------------------------------|---------------------------------------------|------------------------------------|
| 1 | Shopper/Traveller     | easily see what the page is about          | decide if it's relevant to my needs         | Homepage                           |
| 2 | Shopper/Traveller      | view the products                          | choose what I want to buy                   | Product page                       |
| 3 | Shopper/Traveller      | view each product's details                | learn more about its price/description/rating    | Product details page               |
| 4 | Shopper/Traveller      | see product quantities to order more or less | so that I can make a more detailed purchase     | Product details page               |
| 5 | Shopper/Traveller      | sort products                              | locate them quicker by price, name, type    | Product page sort option           |
| 6 | Shopper/Traveller      | search for products                        | find what I'm looking for                   | Search box on homepage             |
| 7 | Shopper/Traveller      | see my search results                      | decide if it's what I want                  | Product page                       |
| 8 | Shopper/Traveller      | see the total of my shopping bag        | stay within my budget                       | Basg page                        |
| 9 | Shopper/Traveller      | see what's in my shopping bag           | make sure I have what I want and the cost   | Basg page                        |
| 10 | Shopper/Traveller      | adjust my bag                           | make easy udates before the checkout        | Bag page                        |
| 11 | Shopper/Traveller      | easily enter my payment information        | pay quickly and confidently                 | Checkout page                      |
| 12 | Shopper/Traveller      | see an order confirmation                  | be sure I've made the correct purchase      | Checkout success page              |
| 13 | Shopper/Traveller      | receive an email copy of my order          | have physical proof of my purchase          | Checkout success page              |
| 14 | Site User   | easily register for an account             | make subsequent purchase quicker            | Register page                      |
| 15 | Site User   | have email confirmation of registering     | be sure it was done correctly               | Register page                      |
| 16 | Site User   | have my own Where Travellers Roam profile                  | store my details and view purchase history  | Profile page                       |
| 17 | Site User   | easily login/logout                        | make subsequent purchases quicker           | Login page                         |
| 18 | Site User   | comment on blog items                      | share my views and show support for trips             | Blog detail page                   |
| 19 | Store Owner | add a product                              | increase my offerings and make more money   | Product management on profile menu |
| 20 | Store Owner | edit a product                             | be sure details and prices are correct      | Product management on profile menu |
| 21 | Store Owner | delete a product                           | remove any out of trend/stock products      | Product management on profile menu |
| 22 | Store Owner | add a blog post                            | inform users of Where Travellers Roam new Blog post and holidays in profile menu    |
| 23 | Store Owner | edit a blog post                           | change the text/image                       | Blog management on profile menu    |
| 24 | Store Owner | delete a blog post                         | remove posts no longer relevant/suitable    | Blog management on profile menu    |



[Back to contents](#contents)

### **Lighthouse**

Lighthouse testing was completed on all pages of the site
- [Home]()
- [Products]()
- [Product Detail]()
- [Bag]()
- [Checkout]()
- [Checkout Success]()
- [Profile]()
- [Blog]()
- [Post Detail]()
- [Add Blog Post]()
- [Add Product]()


### **Validators**

#### **HTML Validator**

#### **CSS Jigsaw**
CSS Jigsaw validation passed for all pages
- [products.css](static/docs/images/validation/jigsaw-product-css.png)
- [blog.css](static/docs/images/validation/jigsaw-blog-css.png)
- [bag.css](static/docs/images/validation/jigsaw-bag-css.png)
- [checkout.css](static/docs/images/validation/jigsaw-checkout-css.png)
- [profile.css](static/docs/images/validation/jigsaw-profile-css.png)
- [style-uni-form.css](static/docs/images/validation/jigsaw-style-uni-form-css.png)
- [uni-form.css](static/docs/images/validation/jigsaw-uni-form-css.png)
- [base.css](static/docs/images/validation/jigsaw-base-css.png)

#### **JSHint**


#### **PEP8**
- Checkout [signals](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1642780620039300) imported but not used in problems tab however this is required as it is being accessed elsewhere so the problem can be ignored.  
- [Line too long](static/docs/images/validation/test_models_problem.png) error in test_models.py however this is required to confirm the test passes.

[With all Python files open](static/docs/images/validation/pep8.png) those are the only two issues.
[Back to contents](#contents)
