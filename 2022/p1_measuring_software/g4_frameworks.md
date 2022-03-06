---
author: Casper Henkes Ana Oprea Krzysztof Baran
title: "The greenest JavaScript Frameworks (How to move to greener JavaScript pastures?)"
date: 03/03/2022
summary: "From famous professional websites to small scale student solutions, everyone uses JavaScript frameworks. In this study, we evaluate the relative power consumption of websites made using Vue, React, Angular, and Svelte. Our tests produced results that suggest that sites in Angular might display more data using less energy than similar sites built using other frameworks."
---

## Introduction

From well-known professional webpages like Google and PayPal to homebrewed webpages made by students for their coursework, everyone is using JavaScript frameworks these days. This is no major surprise, given that these frameworks make developing a website more accessible. It is not that creating web pages cannot be done without these handy tools, but reinventing the wheel is often a tall and usually meaningless task. It has become an industry standard to use it.

The internet uses a lot of energy to run. Just think of the 1 billion hours of video watched daily on sites like YouTube alone [1]. To display this content dynamically, JavaScript is used. If we could make every interaction with the browser just a tiny bit more power efficient, it does not seem like we are making a huge change. All the small bits will add up over time and make an enormous difference.

In this study, we evaluate the relative power consumption of different JavaScript frameworks. We chose to compare these frameworks: Vue, React, Angular, and Svelte as they are popular, and we are more familiar with these frameworks than the other popular frameworks like Ember. By reviewing the power consumption of these frameworks, we hope to educate engineers and consumers alike about power consumption to make a difference eventually.

We believe that, because much effort is put into web programming and engineering of several tools and frameworks that accompany these endeavours, it is essential to investigate how these can impact the sustainability of websites.

## Method

Vue.js, Angular, React, Svelte. We searched for five websites deployed using that framework to have a substantial sample of data for each possibility. The pages that we used were found in two main ways. These sites are listed in the Appendix at the end of this report.

First, we used a chrome addon to detect the framework of the page visited for well-known pages to test what framework they run on. We searched the internet for lists of web pages created using the different frameworks for the rest of the pages. In the first step, we excluded very graphically intensive pages or that were only showing videos. This set of pages was then reduced until we were left with five similar pages per framework to make some comparisons. The lists we consulted for information about the framework used by each of our chosen websites was recently posted.

For all pages, we ran five tests on two different machines using Intel PowerLog [3] to gather the data and Selenium to navigate the web. Each page was visited for at least 30 seconds after each test, allowing the computer to cool down for one minute before starting a new test.

For each page, we then noted down: Which framework it uses, if it shows animations, if it utilizes cookies, if it displays images, if it has video, how many words are on the page, and the total size of the page. The pages were all checked on 02.03.2022, and we used a tool [2] to measure the website storage size. Afterwards, the power consumption data were processed to obtain further insights into the data. The processed data includes the sample mean and the sample variance for each page calculated per machine overall five tests. The page data and the processed power consumption data can be found in the results. We used several scripts to deal with different issues: i) enabling working with webpages such as opening several tabs in browsers with several webpages and being able to scroll through them; ii) fixing a more stable running environment for collecting data about power consumption such as setting the brightness, setting the volume, and setting the size of the window. These are necessary to be able to  provide uniformity between comparisons on different machines or in different running environments; iii) collecting data on various systems and extracting interesting data from the resulting CSV files.

On Windows, the PowerLog [3] retrieves 26 metrics and averages that might account for the most informative data about power consumption. Out of these 26, we focused on Processor Power_0 (Watt). To recreate the measurement, we created a GitHub repository [4] with steps to run the experiments.

## Results

We found key similarities and differences between the results collected from our two different machines: Angular occupied the first position for both devices in terms of the best power consumption, having recorded a value of 9.34 and, respectively, 10.84. Similarly, Vue presented consistent results for both scenarios: 12.34 and 12.76. Consequently, one can infer that Vue performed worse than Angular by 32.11% in the first case and by 17.11% in the second case. However, the discrepancies appeared in the cases of React and Svelte. The former occupied the runner up position with a value of 11.19 for one machine, while dropping to the last position of the 4 with a value of 14.96 for the second machine. The measurements for React were worse than Angular by 19.8% and 38%. Contrastingly, the power consumption for Svelte dropped from 17.74 to 11.37. Of course, these figures represent averages for each of the frameworks.

### Machines

|Specification |Machine 1| Machine 2|
|-----------------|--------------|---------------|
|Model| HP ZBook Studio G3 | HP Envy |
| CPU | Intel(R) Core (TM) i7-6700HQ CPU @ 2.60GHz 2.59 GHz | Intel(R) Core (TM) i7-10750H CPU @ 2.60GHz 2.59 GHz |
| RAM |8 GB | 32 GB |
| OS | Windows 10 Home | Windows 11 Pro |

#### Frameworks

| Framework | Machine 1 (mean) | Machine 2 (mean)|
|:------------|---------:|---------:|
| Vue | 12.3471 | 12.7673 |
| Angular | 9.34379 | 10.8477 |
| React | 11.1962 | 14.963 |
| Svelte | 17.747 | 11.3793 |

#### Websites

| Website | Framework | Machine 1 (mean) | Machine 1 (std)| Machine 2 (mean) | Machine 2 (std)|
|:----------------|:----------------|:------------|---------:|-------- | --- |
| [9gag](https://9gag.com/) | Vue | 10.7822 | 7.98378 | 12.4969 | 13.9895 |
| [gitlab](https://docs.gitlab.com/ee/user/project/issues/) | Vue | 7.28054 | 7.30807 | 8.88004 | 12.1608 |
| [nintendo](https://www.nintendo.co.uk/) | Vue | 11.9746 | 9.4912 | 10.4923 | 14.3784 |
| [euronews](https://www.euronews.com/) | Vue | 16.8066 | 4.99369 | 15.7708 | 15.7535 |
| [torneo](https://www.torneo.ca/) | Vue | 14.0656 | 5.62089 | 16.039 | 11.5926 |
| [db](https://www.db.com/index?language_id=1&kid=sl.redirect-en.shortcut) | Angular | 8.6165 | 8.28137 | 10.43 | 13.7984 |
| [forbes](https://www.forbes.com/) | Angular | 13.6412 | 6.59539 | 13.658 | 15.0884 |
| [paypal](https://www.paypal.com/nl/home/) | Angular | 8.87494 | 7.50366 | 10.7601 | 13.4489 |
| [upwork](https://www.upwork.com/) | Angular | 9.73345 | 8.03935 | 11.9056 | 14.6345 |
| [google](https://www.google.nl/) | Angular | 5.94978 | 7.04896 | 7.44823 | 11.0863 |
| [airbnb](https://www.airbnb.com/) | React | 7.36689 | 8.16244 | 10.1295 | 13.5555 |
| [nytimes](https://www.nytimes.com/) | React | 15.9123 | 7.17729 | 22.8075 | 17.665 |
| [codecademy](https://www.codecademy.com/) | React | 12.4791 | 6.77338| 19.455 | 12.0439 |
| [atlassian](https://www.atlassian.com/) | React | 11.3331 | 7.59099 | 12.8461 | 14.522 |
| [scribd](https://www.scribd.com/) | React | 7.44075 | 7.90974 | 9.58939 | 12.9471 |
| [spotify](https://www.spotify.com/nl/about-us/contact/) | Svelte | 6.42971 | 7.36925 | 8.26042 | 11.7758 |
| [note](https://note.com/) | Svelte | 9.05317 | 6.84902 | 10.8866 | 12.6283 |
| [squareup](https://squareup.com/us/en/) | Svelte | 13.2312 | 6.92621 | 12.8612 | 15.1846 |
| [templatemonster](https://www.templatemonster.com/) | Svelte | 27.0491 | 4.44424 | 12.6098 | 15.1223 |
| [sentry](https://sentry.io/welcome/) | Svelte | 26.4186 | 3.82589 | 12.2433 | 14.7747 |

## Key Findings

It is impossible to compare websites (and thus also the performance of frameworks) only using the power consumed. Some pages will show the user a lot more information. For example, take a remarkably simple web page only showing one image that consumed a small amount of energy and compare this page to a website like Facebook. Facebook will quite likely use up more power. However, you cannot really say that it is less efficient as it shows the user more. We decided that to get around this issue, and we would compare the page's energy usage and then compare that to pages of comparable size and, if possible, word count as an estimate to measure how much a page is showing the user. However, an interesting point can be made about minimalistic web pages that do not add unnecessary features. Perfect examples of this are the Google and Spotify pages. Super minimalistic and optimized just to fulfil their purpose and nothing more. Good to see is that they also score well when measuring the power consumption.

One metric that raised our attention is the standard deviation. It seemed high compared to the average power consumption per test generated by PowerLog, which gives a lot more consistent value. The high standard deviation can be explained with the test data. There are quite many variances in the power consumption during the test. For example, the start-up is more power-intensive than the end of the test. The difference between the variance between the two machines is less easy to explain. It could be that the pages can vary wildly in their power consumption, however, it is also possible that it was the result of some background process running though we did our best to stop as many background processes as possible.

From our results, it seems that Angular is the most power-efficient framework. It is, however, not enough to have the least power consumption. It is possible that the Angular sites had to load much less data than the other sites and were thus able to use less power. To test this, we compare two angular sites, Forbes, and PayPal, two comparable sites in size and features built-in other frameworks. We compared Forbes to Euronews. Euronews's page size is a slightly smaller page in terms of MB that does include more text and does not include ads. However, despite being smaller and having no ads, Euronews does consume more power than Forbes. Code academy is a slightly larger page when compared to Forbes while not running ads. Its consumers spend less energy on machine 1 but more on machine 2, which might be similar overall. PayPal is one of our larger pages, but it consumes very little power. The closest site in size with the same noted features is a sentry. And while the results for sentry seem to vary wildly between machines 1 and 2, it still consumes more power than PayPal does while being slightly smaller in size.

## Limitations

One limitation of this study is that the ranking of power consumption between our two test machines varied a lot for specific pages. The websites may differ wildly in their power consumption depending on the time of day they are in use. However, we cannot rule out that this discrepancy comes from some background or another factor. We think that the results still show that the Angular pages are more efficient as on both machines, the Angular pages consistently outperform the other frameworks.

It is essential to acknowledge that a locally running PowerLog is not the end all be all for testing power consumption. First, it is very dependent on the local setup of the user. As an example, there are several daemons background processes or bloatware that are not controllable or visible, and these factors influence the power consumption registered by PowerLog. To try to mitigate this, we ran every test several times in the same session without the user changing anything else on the machine in between. This helps keep the background processes similar across the different runs. Then running PowerLog locally also does not consider the power consumed by the server serving the webpage. As we have no access to the web servers used by these pages, we cannot log or otherwise influence this, and this study assumes that it will be similar across pages and frameworks. An interesting follow-up study would be to test this assumption.

This study is also very prone to selection bias. There was no complete list of pages created using the frameworks available to randomly select pages from. And thus, we relied on other sources to find pages. It is possible that we accidentally selected pages that paint a different picture than the real situation. Furthermore, in the case of 9gag, as one can infinitely scroll through the page, it was not appropriate to gather data about the website size and the number of words. We tried to mitigate this by first starting off with a more extensive selection of pages and then selecting pages that seemed similar enough to each other. But this process again is subject to bias, which we tried to mitigate by peer reviewing and discussing the pages selected. This method of selecting pages could work; however, it was our first time doing so, and we cannot claim to be experts in selecting similar pages.

We also do not have access to the source code of most web pages we tested. Viewing the source code would allow us to delve into the more profound features and make better comparisons between frameworks. On top of that, some of these websites could be using bad practices for using the framework or JavaScript, which we could not be readily aware of. One way to get around this is to implement the same web pages in different frameworks using (as far as that is possible) the exact same features and then testing the power consumption. One could design several web benchmarks like image processing (for testing CPU heavy processing), text-only (measure how much overhead frameworks add), video playing (test content loading), infinite scrolling pages (like social media to test lazy scrolling), etc. This is, however, very time consuming and was not feasible for this project.

Another important note are cookies and the browser cache. The web drivers we used for the test created a new instance for each session so cookies would be reset. However, we could not confirm or deny that the web driver reset the browser cache as well. To mitigate this issue, we ran the test another time before the actual test so that the web driver would have opened and loaded every page already once. Another feasible way to mitigate this would be to research where the cache is stored and how to refresh it automatically.

Due to time constraints, we decided to stop at five runs per page and run the tests on two machines. More runs per page would have helped shape a clearer picture of what is truly happening. Running the tests on more and different devices would allow us to verify whether the results hold in general or are the result of the specific setup used to test it.

## Conclusions

We believe that the problem of power consumption and green websites should be treated carefully by front-end developers. Apart from having nice-looking websites with which the users can easily interact, one should also consider how to optimize the power consumption and the selection of a framework that could already help with that goal.

Our study suggests that sites in Angular can display more data using less energy than comparable sites built using other frameworks. PayPal is an interesting page as it is incredibly low on the energy consumption scale while having one of the larger pages. If it is not the framework that matters, then the engineers at PayPal have created a wonderfully green page that uses a minimal number of resources while having a high-quality user experience. We could all learn from.

## Appendix:

### Website Details

| **Website** | **Type ** | **Animations ** | **Ads ** | **Cookies ** | **Images ** | **Nr Words ** | **Website size ** | **Videos ** |
|:----------------------:|:---------:|:---------------:|:--------:|:------------:|:-----------:|:-------------:|:-----------------:|:-----------:|
| 9gag | Vue.js | no | yes | yes | yes |??? | ??? | yes |
| Gitlab docs | Vue.js | no | no | yes | no | 521 | 1 MB | no |
| Nintendo | Vue.js | yes | no | yes | yes | 654 | 4.1 MB | no |
| Euronews | Vue.js | yes | no | yes | yes | 2404 | 1.5 MB | no |
| Torneo | Vue.js | yes | no | yes | yes | 407 | 5 MB | yes |
| Deutsche Bank | Angular | yes | No | yes | yes | 659 | 1.5 MB | yes |
| Forbes | Angular | yes | yes | yes | yes | 720 | 1.7 MB | no |
| PayPal | Angular | yes | no | yes | no | 228 | 2.4 MB | no |
| Upwork | Angular | no | no | yes | yes | 478 | 844.3 kB | no |
| Google | Angular | no | no | yes | no | 17 | 802.3 kB | no |
| Airbnb | React | yes | no | yes | yes | 310 | 1.2 MB | no |
| New York Times | React | no | yes | yes | yes | 2268 | 3.2 MB | yes |
| Code Academy | React | yes | no | yes | yes | 449 | 1.8 MB | no |
| Atlassian | React | yes | no | yes | yes | 462 | 3.4 MB | no |
| Scribd | React | no | no | yes | yes | 369 | 3.4 MB | no |
| Spotify Contact page | Svelte | no | no | yes | no | 490 | 427.7 kB | no |
| Note | Svelte | no | no | yes | yes | 976 | 14.7 MB | no |
| Square Up | Svelte | yes | no | yes | yes | 774 | 1.2 MB | no |
| Template Monster | Svelte | no | yes | yes | yes | 1458 | 3 MB | no |
| Sentry | Svelte | no | no | yes | yes | 558 | 2.1 MB | no |

We included a replication package for systems with Windows OS.

### Framework research list

* Angular
	* [https://www.monocubed.com/blog/websites-built-with-angular/](https://www.monocubed.com/blog/websites-built-with-angular/)
* Vue
	* [https://www.techuz.com/blog/top-9-websites-built-using-vue-js/](https://www.techuz.com/blog/top-9-websites-built-using-vue-js/)
	* [https://madewithvuejs.com/euronews](https://madewithvuejs.com/euronews)
	* [https://madewithvuejs.com/torneo](https://madewithvuejs.com/torneo)
* React
	* [https://www.monocubed.com/blog/websites-built-with-react/](https://www.monocubed.com/blog/websites-built-with-react/)
* Svelte
	* [https://www.wappalyzer.com/technologies/javascript-frameworks/svelte](https://www.wappalyzer.com/technologies/javascript-frameworks/svelte)
### Extensions

* [Angular](https://chrome.google.com/webstore/detail/angular-devtools/ienfalfjdbdpebioblfackkekamfmbnh)
* [React](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)
* [Vue](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?hl=en)
* [Svelte](https://chrome.google.com/webstore/detail/svelte-devtools/ckolcbmkjpjmangdbmnkpjigpkddpogn#:~:text=Svelte%20Devtools%20is%20a%20Chrome,new%20tab%20in%20Chrome%20DevTools.)

  
## References:

[1] Aslam, S. (2022, January 2). YouTube by the numbers: Stats, Demographics & Fun Facts. Omnicore. Retrieved March 3, 2022, from [https://www.omnicoreagency.com/youtube-statistics/](https://www.omnicoreagency.com/youtube-statistics/)

[2] SolarWinds Worldwide. (n.d.). Pingdom Tools. Website Speed Test. Retrieved March 3, 2022, from https://tools.pingdom.com/

[3] McKay, T., & Konsor, P. C. (2014, July 1). Intel® Power Gadget. Intel. Retrieved March 3, 2022, from [https://www.intel.com/content/www/us/en/developer/articles/tool/power-gadget.html](https://www.intel.com/content/www/us/en/developer/articles/tool/power-gadget.html)

[4] Baran, K., Henkes, C., & Oprea, A. (2022). The greenest JavaScript Frameworks (How to move to greener JavaScript pastures?) (Version 1.0.0) [Computer software]. https://github.com/kbaran1998/energy-comsumption-project
