-> There is a limit on how much you can do. From my testing its between 50-100. Then it will return a Error.
-> Make sure that the website are in the same folder as this code.
-> Make sure that the Excel CSV has a list of only websites, in the follwing format.
  ...........
  Colum 1 : Website --> Have this title on the First Row and Columme or Remove "next(csv_reader)" from the code. Up to you.
  Colum 2 : Your Website that you want to do
  ........
  -> Refer to the Template

This is the GET THE BARD KEY:
 1) Go to Bard.com 
 2) Login using your Email and Password
 3) Right-Click
 4) Inspect Element
 5) Application (Its at the top tabs)
 6) Under Storage, Go on Cookies
 7) Click on "Http://bard.google.com"
 8) Click on "__Secure-1PSID". IMPORTANT: THE VALUES OF THE COOKIE MUST END WITH A PERIOD.
 9) Copy the Value and paste below into varible "os.environ["_BARD_API_KEY"]". Eg os.environ["_BARD_API_KEY"] = "Your Cookie Value". Make Sure they have speach marks there.


 
