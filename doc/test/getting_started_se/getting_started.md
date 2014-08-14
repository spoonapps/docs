# Getting Started: Selenium

Running your tests on Spoonium is almost exactly like running them on a local Selenium Grid. What does this mean for you?

1. Porting your tests to run on Spoonium requires very few changes.
2. You can use native Selenium APIs - no extra dependencies or libraries to import. 

The key difference is that Spoonium takes care of all the Selenium infrastructure and networking for you! Point your tests to the Spoonium hub at `http://localhost:4444/wd/hub` and Spoonium will automatically provision, stream, and start the test on the required browser.

If you've never used Selenium before, try our [Beginner Tutorial](TODO: add link).

If you've used a different cloud-based testing service in the past, check out the [Adapting Tests from Other Services](TODO: add link) page.

If you're a Selenium veteran, but you've never used Selenium Grid before, you'll need to change a couple lines of code in your tests. Instructions vary slightly between languages, so find your preferred language below for specific instructions.

Don't see your preferred language? Let us know and we'll help you get started. 

[Getting Started: Java](TODO: add link)

[Getting Started: C#](TODO: add link)

[Getting Started: Python](TODO: add link)

If you're already using Grid to run your tests, configuring your tests for Spoonium is a one-line change. Substitute the URL of your current Grid with `http://localhost:4444/wd/hub` and you're ready to go!

## Supported Browsers

- Chrome 27+ 
- Firefox 3+
- Internet Explorer 6+

*Don't see your preferred browser? [Let us know](mailto:support@spoonium.net) and we'll do our best to get it added.*