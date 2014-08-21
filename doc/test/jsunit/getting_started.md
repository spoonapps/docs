## Getting Started: JavaScript Unit Testing

In addition to Selenium testing, Spoonium also offers cross-browser JavaScript unit testing. 

Any browser available in the Spoonium Grid can be used for JS unit testing. You can use any of the most popular JS unit testing frameworks on Spoonium. All you need is a compatible test runner, such as Karma or Mocha. 

#### How it Works

JS unit testing on Spoonium leverages the same infrastructure as our Selenium testing. Thus, your test runner must support launching browsers via Selenium WebDriver. If your runner has a plugin that can interact with a Selenium Grid, it should work on Spoonium. The only adaptation you should need to make is to set the Selenium `host` or `hostname` to `localhost` and the port to `4444`.

In the **Supported Test Runners** section, below, you'll find a list of test runners that we have tested and confirmed work with Spoonium. If you are using a different test runner and are having problems configuring it for Spoonium, email our support team and we'll be happy to help out.

#### Supported Browsers

- Chrome 27+ 
- Firefox 3+
- Internet Explorer 6+

*Don't see your preferred browser? [Let us know](mailto:support@spoonium.net) and we'll do our best to get it added.*

#### Supported Test Runners

**Karma** ([on Github](http://github.com/karma-runner/karma))

To learn how to configure Karma for Spoonium see [Getting Started: Karma](TODO: add link). 

- For a list of frameworks Karma supports, see: [http://npmjs.org/browse/keyword/karma-plugin](http://npmjs.org/browse/keyword/karma-plugin). 
- If you want to learn a little more about Karma, check out the [Karma homepage](http://karma-runner.github.io/0.12/index.html). 

**Mocha/Mochify** ([on Github](http://github.com/mantoni/mochify.js))

To learn how to configure Mocha/Mochify for Spoonium, see [Getting Started: Mocha](TODO: add link). 

- Mochify only supports the [Mocha](http://visionmedia.github.io/mocha/) framework. 