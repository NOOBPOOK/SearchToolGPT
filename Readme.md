This program acts as a Search tool to go along with Guidance framework.
It uses GPT-3.5 turbo and uses google search to help along to do online searching on the web.
It uses google-search-results module and requires a SERPAPI Key to be stored in an .env file

You can ask this agent any news or recent information. Based on its training set, if it is able to answer he answers that
itself, otherwise he uses the tool to search for the information online.
Once the tool return the search results, the agent tries to frame the answser in a complete sense and return to the user.