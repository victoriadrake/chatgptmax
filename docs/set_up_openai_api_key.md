# Set up your OpenAI API key

To set up your OpenAI API key for using the `chatgptmax` module, follow these steps:

1. **Sign up for an OpenAI Account**: If you don't already have an account, visit the [OpenAI website](https://openai.com/) and sign up for a free or paid account.

2. **Access Your API Key**:
   - After signing in to your OpenAI account, go to the [OpenAI API](https://platform.openai.com/signup) page.
   - If you haven't done so already, you may need to join the waitlist for access to the API.
   - Once you have access, you'll be able to generate an API key.

3. **Generate an API Key**:
   - On the OpenAI API page, click on "Create API Key."
   - Give your API key a name or description to help you identify its purpose (e.g., "chatgptmax").
   - Click on "Generate API Key."

4. **Copy Your API Key**:
   - Once the API key is generated, you'll see it displayed on the page.
   - Copy the API key to your clipboard.

5. **Set Up Your Environment Variable**:
   - To securely store your API key, set it as an environment variable on your local machine or in your CI/CD environment. This ensures that you don't accidentally expose your key in your code.
   - The exact process for setting environment variables may vary depending on your operating system:

     - **Windows**:
       - Open the Start Menu and search for "Environment Variables."
       - Click on "Edit the system environment variables."
       - In the System Properties window, click the "Environment Variables" button.
       - Under "User variables" or "System variables," click "New" to add a new environment variable.
       - Enter "OPENAI_API_KEY" as the variable name.
       - Paste your API key as the variable value.
       - Click "OK" to save the variable.

     - **macOS** and **Linux**:
       - Open a terminal window.
       - To set the API key for the current session, use the following command:

         ```sh
         export OPENAI_API_KEY=your_api_key_here
         ```

       - To make this change permanent, you can add the export command to your shell's profile file (e.g., `.bashrc`, `.zshrc`, or `.profile`).

6. **Verify the Setup**:
   - To verify that your API key is set up correctly, you can open a terminal or command prompt and type the following command:

     ```sh
     echo $OPENAI_API_KEY
     ```

   - If your API key is set correctly, it should display your API key.

Now your OpenAI API key is set up as an environment variable, and you can use it with the `chatgptmax` module for various text processing tasks. Make sure to keep your API key secure and do not share it publicly or commit it to version control systems.
