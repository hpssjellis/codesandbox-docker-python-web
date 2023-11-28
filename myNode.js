// This function will take an argument and return it

myHTML = `   
<form method="POST">
  Enter your input: <input type="text" name="user_input">
  <input type="submit" value="Submit">
</form>
`;

function myEchoArgument(myArgument) {
  return myHTML + myArgument;
}

// Retrieving the argument passed to the script
const myArgument = process.argv[2];

// Check if the argument is provided
if (myArgument) {
  console.log("Received argument:", myEchoArgument(myArgument));
} else {
  console.error("No argument provided. Please provide an argument.");
  process.exit(1);
}
