<h1 align="center" dir="rtl">
<br>
  <a href="https://github.com/thedaviddias/Front-End-Performance-Checklist"><img src="https://raw.githubusercontent.com/thedaviddias/Front-End-Performance-Checklist/master/images/logo-front-end-performance-checklist.jpg" alt="Front-End Performance Checklist" width="170"></a>
  <br>
  <br>
  چک لیست کارایی در فرانت‌اند
  <br>
</h1>

<h4 align="center" dir="rtl">یک ترجمه مفهومی از <a href="https://github.com/thedaviddias/Front-End-Performance-Checklist">Front-End Performance Checklist</a></h4>
<h4 align="center" dir="rtl">🎮 تنها چک لیست مربوط به مباحث کارایی در فرانت‌اند که نسبت به بقیه سریع‌تر اجرا میشه</h4>
<p align="center" dir="rtl">یه قانون ساده: "با در نظر گرفتن کارایی در ذهنتون، طراحی و برنامه‌نویسی کنین"</p>

<p align="center">
  <a href="http://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
  </a>
  <a href="https://discord.gg/btHQRkm">
    <img src="https://img.shields.io/badge/chat-on_discord-4837E2.svg?style=flat-square" alt="Discord">
  </a>
    <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="Licence MIT">
  </a>
</p>

<p align="center" dir="rtl">
  <a href="#نحوه-استفاده">نحوه استفاده</a> • <a href="#همکاری">همکاری</a>
</p>

<p align="center">
  <a href="https://github.com/thedaviddias/Front-End-Performance-Checklist">🇪🇳</a>
  <a href="https://github.com/JohnsenZhou/Front-End-Performance-Checklist">🇨🇳</a>
  <a href="https://github.com/WilliamDASILVA/Front-End-Performance-Checklist">🇫🇷</a>
  <a href="https://github.com/ParkSB/Front-End-Performance-Checklist">🇰🇷</a>
  <a href="https://github.com/fernandofawkes/Front-End-Performance-Checklist">🇵🇹</a>
  <a href="https://github.com/lex111/Front-End-Performance-Checklist">🇷🇺</a>
  <a href="https://github.com/GameWith/Front-End-Performance-Checklist">🇯🇵</a>
</p>

<h2 dir="rtl">جدول محتوا</h2>

<ol dir="rtl">
  
<li>
  
  **[HTML](#HTML)**

</li>
<li>
  
  **[CSS](#CSS)**
  
</li>
<li>
  
  **[فونت ها](#فونت-ها)**

</li>
<li>
  
  **[تصاویر](#تصاویر)**

</li>
<li>
  
  **[جاوا اسکریپت](#جاوا-اسکریپت)**
  
</li>
<li>
  
  **[سرور](#سرور) (در حال تکمیل شدن)**

</li>
<li>
  
  **[فریم‌ورک‌های جاوا اسکریپت](#performances-and-js-frameworks) (در حال تکمیل شدن)**
 
</li>

</ol>

<h2 dir="rtl">معرفی</h2>

<p dir="rtl">
کارایی یک موضوع بزرگی است و همیشه مربوط به "بک‌اند" و یا یک "مدیر" نیست؛ بلکه "فرانت‌اند" هم در این زمینه مسئولیت‌هایی دارد. چک لیست کارایی فرانت‌اند، یک لیست کامل از مواردی است که شما باید به عنوان یک توسعه‌دهنده فرانت‌اند، آن‌ها را بررسی کنید و یا حداقل از وجود این موارد آگاه شوید و این موارد را در پروژه‌های خود (از پروژه‌های شخصی تا پروژه‌های حرفه‌ای) اعمال کنید.
</p>

<h3 dir="rtl">نحوه استفاده</h3>

<p dir="rtl">
  برای هر یک از قوانین، یک بند وجود دارد که توضیح می‌دهد <em>چرا</em> این قانون مهم است و <em>چگونه</em> می‌توانید آن را رفع کنید. برای اطلاعات بیشتر نیز به سراغ لینک‌های بروید که به عنوان 🛠 ابزار، 📖 مقاله و یا 📹 رسانه علامت گذاری شده‌اند و می‌توانند مکمل این چک لیست باشند.
</p>
<p dir="rtl">
تمامی موارد در <strong>چک لیست کارایی فرانت‌اند</strong> برای رسیدن به بالاترین امتیاز کارایی ضروری و مهم هستند اما شما علامت‌هایی را می‌بینید که به شما در الویت بندی این قوانین (جهت بررسی و اعمال) کمک می‌کنند. در مجموع 3 شاخص برای تعیین الویت وجود دارند: 
</p>

<ul dir="rtl">
  
<li>
  
![Low][low] به این معنی است که این مورد الویت **پایین** دارد.
  
</li>
<li>

![Medium][medium] به این معنی است که این مورد الویت **متوسط** دارد. شما نباید از این موارد صرف نظر کنید.

</li>
<li>

![High][high] به این معنی است که این مورد الویت **بالا** دارد. شما نمی‌توانید در استفاده از این مورد خودداری کنید و حتما باید موارد توصیه شده را رعایت کنید.

</li>

</ul>

<h3 dir="rtl">ابزارها</h3>

<p dir="rtl">
  لیستی از ابزارها که شما می‌توانید با استفاده از آن‌ها وبسایت یا اپلیکیشن خود را بررسی و بازبینی کنید:
</p>

 * 🛠 [WebPagetest - Website Performance and Optimization Test](https://www.webpagetest.org/)
 * 🛠 ☆ [Dareboost: Website Speed Test and Website Analysis](https://www.dareboost.com/) (use the coupon WPCDD20 for -20%)
 * 🛠 [Treo: Page Speed Monitoring](https://treo.sh/?ref=perfchecklist)
 * 🛠 [GTmetrix | Website Speed and Performance Optimization](https://gtmetrix.com/)
 * 🛠 [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)
 * 🛠 [Web.dev](https://web.dev/measure)
 * 🛠 [Pingdom Website Speed Test](https://tools.pingdom.com)
 * 📖 [Make the Web Faster | Google Developers](https://developers.google.com/speed/)
 * 🛠 [Sitespeed.io - Welcome to the wonderful world of Web Performance](https://www.sitespeed.io/)
 * 🛠 [Calibre](https://calibreapp.com/)
 * 🛠 [Website Speed Test | Check Web Performance &raquo; Dotcom-Tools](https://www.dotcom-tools.com/website-speed-test.aspx)
 * 🛠 [Website and Server Uptime Monitoring - Pingdom](https://www.pingdom.com/product/uptime-monitoring/) ([Free Signup Link](https://www.pingdom.com/free))
 * 🛠 [Uptime Robot](https://uptimerobot.com)
 * 🛠 [SpeedCurve: Monitor front-end performance](https://speedcurve.com)
 * 🛠 [PWMetrics - CLI tool and lib to gather performance metrics](https://github.com/paulirish/pwmetrics)
 * 🛠 [Varvy - Page speed optimization]( https://varvy.com/pagespeed/)
 * 🛠 [Lighthouse - Google]( https://developers.google.com/web/tools/lighthouse/#devtools)
 * 🛠 [Checkbot browser extension - Checks for web performance best practices](https://www.checkbot.io/)
 * 🛠 [Yellow Lab Tools | Online test to help speeding up heavy web pages](https://yellowlab.tools/)
 * 🛠 [Speedrank - Web Performance Monitoring](https://speedrank.app/)
 * 🛠 [DebugBear - Monitor website performance and Lighthouse scores](https://www.debugbear.com/)
 * 🛠 [packtracker.io - Check your webpack bundle size on every pull request.](https://packtracker.io/)
 * 🛠 [Exthouse - Analyze the impact of a browser extension on web performance](https://github.com/treosh/exthouse)
 * 🛠 [LogRocket - Measure front-end performance in production apps](https://logrocket.com)


<h3 dir="rtl">منابع</h3>

 * 📹 [The Cost Of JavaScript - YouTube](https://www.youtube.com/watch?v=_bzqF05xsC4) ([text version](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4))
 * [AddyOsmani.com - Start Performance Budgeting](https://addyosmani.com/blog/performance-budgets/)
 * 📖 [Get Started With Analyzing Runtime Performance  |  Google Developers](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/)
 * 📖 [State of the Web | 2018_01_01](https://httparchive.org/reports/state-of-the-web?start=2018_01_01)
 * 📖 [Page Weight Doesn't Matter](https://www.speedshop.co/2015/11/05/page-weight-doesnt-matter.html)
 * 📖 [Front-End Performance Checklist 2021 [PDF, Apple Pages, MS Word]](https://www.smashingmagazine.com/2021/01/front-end-performance-2021-free-pdf-checklist/)
 * 📖 [Designing for Performance Weighing Aesthetics and Speed - By Lara Callender Hogan [eBook, Print]](http://designingforperformance.com/index.html)
 * 📖 [Varvy - Web performance glossary](https://varvy.com/performance/)
 * 📖 [fabkrum/web-performance-resources: Up to date collection of valuable web performance resources](https://github.com/fabkrum/web-performance-resources)
 * 📖 [Checkbot - Web Speed Best Practices](https://www.checkbot.io/guide/speed/)
 * 🛠 [Progressive Tooling - A list of community-built, third-party tools that can be used to improve page performance](https://progressivetooling.com/)

---

## HTML

![html]

- [ ] **Minified HTML:** ![medium] &#x202b;کدهای HTML باید خلاصه‌سازی شده و کامنت‌ها، فضاهای خالی و خطوط اضافی حذف شوند

    *چرا&#x202b;:*
    > &#x202b;حذف فضاهای خالی، کامنت‌ها و هر مورد غیر ضروری دیگر باعث کاهش اندازه صفحه HTML شما شده و سرعت بارگزاری صفحه را افزایش می‌دهد و در نهایت کاربران حجم کمتری را برای دانلود صرف می‌کنند.

    *&#x202b;چگونه:*
    > &#x202b;بیشتر فریم ورک‌ها، ابزارهایی دارند که وظیفه آن‌ها خلاصه کردن کدهای HTML است. شما می‌توانید از بسته‌های موجود در NPM که اینکار را به صورت خودکار انجام می‌دهند نیز استفاده کنید.

    * 🛠 [HTML minifier | Minify Code](http://minifycode.com/html-minifier/)
    * 🛠 [Online HTML Compressor](http://refresh-sf.com)
    * 📖 [Experimenting with HTML minifier — Perfection Kills](http://perfectionkills.com/experimenting-with-html-minifier/#use_short_doctype)
   
- [ ] **Place CSS tags always before JavaScript tags:** ![high] &#x202b;اطمینان حاصل کنید که CSS پیش از کدهای جاوا اسکریپت قرار گیرد

    ```html
    <!-- توصیه نمی‌شود -->
    <script src="jquery.js"></script>
    <script src="foo.js"></script>
    <link rel="stylesheet" href="foo.css"/>

    <!-- توصیه می‌شود -->
    <link rel="stylesheet" href="foo.css"/>
    <script src="jquery.js"></script>
    <script src="foo.js"></script>
    ```

    *&#x202b;چرا:*
    > &#x202b;قرار دادن CSS پیش از جاوا اسکریپت، قابلیت دانلود بهتر و موازی را فراهم می‌کند و این امر باعث افزایش سرعت در هنگام رندر مرورگر می‌شود.

    *&#x202b;چگونه:*
    > &#x202b;اطمینان حاصل کنید `<link>` و `<style>` موجود در بخش `<head>` همیشه قبل از `<script>` قرار داشته باشند.

    * 📖 [Ordering your styles and scripts for pagespeed](https://varvy.com/pagespeed/style-script-order.html)

- [ ] **Minimize the number of iframes:** ![high] &#x202b;تنها در صورتی از iframe استفاده کنید که قادر به استفاده از روش دیگری نباشید. البته نهایت تلاش خود را به‌کار بگیرید تا حد امکان از iframe استفاده نکنید

- [ ] **Pre-load optimization with prefetch, dns-prefetch and prerender:** ![low] &#x202b;مرورگرهای پراستفاده می‌توانند با استفاده از تگ `<link>` و صفت `rel` با مقادیر مشخص، آدرس‌های خاصی را پیش بارگزاری (pre-loading) کنند

    *&#x202b;چرا:*
    > &#x202b; امکان Prefetching به مرورگر اجازه می‌دهد تا مخفیانه منابع ضروری را که در آینده برای نشان دادن محتوا به کاربر مورد استفاده قرار می‌گیرند را دریافت کند. مرورگر قادر است این منابع را در کش خود ذخیره کند و باعث افزایش سرعت بارگزاری شود. زمانی که بارگزاری صفحه جاری به پایان رسید و پردازنده بیکار (idle) شد، مرورگر شروع به دانلود این منابع می‌کند؛ و زمانی که کاربر بر روی یک لینک مشخص کلیک می‌کند (در حالی که منابع مورد نیاز برای بارگزاری آن از قبل دریافت شده)، محتوا سریعا برای کاربر نمایش داده خواهد شد. 

    *&#x202b;چطور:*
    > &#x202b;مطمئن شوید که قابلیت‌های تگ `<link>` به درستی در بخش `<head>` استفاده کنید.

    * 📖 [What Is Prefetching and Why Use It](https://www.keycdn.com/support/prefetching)
    * 📖 [Prefetching, preloading, prebrowsing](https://css-tricks.com/prefetching-preloading-prebrowsing/)
    * 📖 [What is Preload, Prefetch, and Preconnect](https://www.keycdn.com/blog/resource-hints)

**[⬆ &#x202b;برگشت به بالا](#جدول-محتوا)**

## CSS

![css]

- [ ] **Minification:** ![high] &#x202b;کدهای CSS باید خلاصه‌سازی شده و کامنت‌ها، فضاهای خالی و خطوط اضافی حذف شوند

    *&#x202b;چرا:*
    > &#x202b;زمانی که فایل‌های CSS خلاصه‌سازی می‌شوند، محتوا سریع‌تر بارگزاری شده و کاربر داده کمتری را دانلود می‌کند. خلاصه‌سازی فایل‌های CSS در خروجی نهایی بسیار مهم است. انجام این عمل هم به نفع کاربر و هم به نفع کسب و کاری است که قصد دارد هزینه پهنای باند و استفاده از منابع را کاهش دهد.

    *&#x202b;چگونه:*
    > &#x202b;از ابزارهایی استفاده کنید که فایل‌های مورد نظر را به صورت خودکار در زمان تولید خروجی نهایی و یا پیش از آن خلاصه‌سازی کنند.

    * 🛠 [cssnano: A modular minifier based on the PostCSS ecosystem. - cssnano](https://cssnano.co/)
    * 🛠 [CSS Minfier](https://goonlinetools.com/css-minifier/)
    * 🛠 [@neutrinojs/style-minify - npm](https://www.npmjs.com/package/@neutrinojs/style-minify)
    * 🛠 [Online CSS Compressor](http://refresh-sf.com)


- [ ] **Concatenation:** ![medium] &#x202b;فایل‌های CSS در یک فایل ادغام شوند *(ممکن است برای HTTP/2 نیازی نباشد)*.

    ```html

    <!-- توصیه نمی‌شود -->
    <link rel="stylesheet" href="foo.css"/>
    <link rel="stylesheet" href="bar.css"/>

    <!-- توصیه می‌شود -->
    <link rel="stylesheet" href="foobar.css"/>
    ```

    *&#x202b;چرا:*
    > &#x202b;اگر شما هنوز هم از HTTP/1 استفاده می‌کنید، لازم است تا فایل‌های CSS را با هم ادغام کنید. ممکن است انجام این عمل زمانی که شما از HTTP/2 استفاده می‌کنید نیازی نباشد. (تست و بررسی بیشتر باید انجام گیرد)

    *&#x202b;چگونه:*
    > - &#x202b;از ابزارهای آنلاین یا هر پلاگین دیگری که در زمان تولید خروجی نهایی و یا پیش از آن، فایل‌های CSS را با هم ادغام می‌کنند استفاده کنید. <br>
    > - &#x202b;البته اطمینان حاصل کنید که این ادغام باعث ایجاد مشکل در پروژه شما نشود.

    * 📖 [HTTP: Optimizing Application Delivery - High Performance Browser Networking (O'Reilly)](https://hpbn.co/optimizing-application-delivery/#optimizing-for-http2)
    * 📖 [Performance Best Practices in the HTTP/2 Era](https://deliciousbrains.com/performance-best-practices-http2/)

- [ ] **Non-blocking:** ![high] &#x202b;فایل‌های CSS باید به گونه‌ای بارگزاری شوند که ایجاد DOM به تاخیر نیفتد

    ```html
    <link rel="preload" href="global.min.css" as="style" onload="this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="global.min.css"></noscript>
    ```

    *&#x202b;چرا:*
    > &#x202b;فایل‌های CSS می‌توانند تا مدتی بارگزاری ادامه محتویات صفحه شما را با تاخیر مواجه کند. با استفاده از قابلیت `preload` می‌توان بارگذاری فایل‌های CSS را پیش پردازش کدهای موجود در صفحه آغاز کرد.

    *&#x202b;چطور:*
    > &#x202b;تنها با افزودن صفت `rel` همراه با مقدار `preload` و اضافه کردن `"as="style` به تگ `<link>` این امر امکان پذیر است.

    * 🛠 [loadCSS by filament group](https://github.com/filamentgroup/loadCSS)
    * 📖 [Example of preload CSS using loadCSS](https://gist.github.com/thedaviddias/c24763b82b9991e53928e66a0bafc9bf)
    * 📖 [Preloading content with rel="preload"](https://developer.mozilla.org/en-US/docs/Web/HTML/Preloading_content)
    * 📖 [Preload: What Is It Good For? — Smashing Magazine](https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/)

- [ ] **Unused CSS:** ![medium] &#x202b;قوانین بدون استفاده را حذف کنید

    *&#x202b;چرا:*
    > &#x202b;حذف قوانین بدون استفاده در CSS می‌تواند باعث کاهش حجم فایل‌ها شود و در نهایت سرعت بارگزاری فایل‌ها را بیشتر کند.

    *&#x202b;چطور:*
    > &#x202b;⚠️ همیشه فریم‌ورک‌های مورد استفاده‌تان را بررسی کنید تا کدهای اضافی نداشته باشند. بیشتر اوقات شما به تمامی قوانین موجود در این فریم‌ورک‌ها احتیاج نخواهید داشت.

    * 🛠 [UnCSS Online](https://uncss-online.com/)
    * 🛠 [PurifyCSS](https://github.com/purifycss/purifycss)
    * 🛠 [PurgeCSS](https://github.com/FullHuman/purgecss)
    * 🛠 [Chrome DevTools Coverage](https://developers.google.com/web/updates/2017/04/devtools-release-notes#coverage)

* [ ] **CSS Critical:** ![high] &#x202b;CSSهای ضروری ("critical" یا "above the fold") شامل مجموعه قوانین CSS هستند که برای نمایش بخشی از صفحه که در حال نمایش (در زمان بارگزاری) است، می‌باشند. این قوانین پیش از خطوط تعریف فایل‌های CSS و در داخل تگ `<style>` قرار میگیرند. 

    *&#x202b;چرا:*
    > &#x202b;استفاده از CSSهای ضروری باعث افزایش سرعت در رندر صفحات می‌شود و همچنین تعداد درخواست‌ها به سرور را کاهش می‌دهد.

    *&#x202b;چگونه:*
    > &#x202b;CSSهای ضروری را  با استفاده از ابزارهای آنلاین و یا پلاگین‌های موجود (مثلا ابزاری که Addy Osmani توسعه داده است) تولید کنید.

    * 📖 [Understanding Critical CSS](https://www.smashingmagazine.com/2015/08/understanding-critical-css/)
    * 🛠 [Critical by Addy Osmani on GitHub](https://github.com/addyosmani/critical) automates this.
    * 📖 [Inlining critical CSS for better web performance | Go Make Things](https://gomakethings.com/inlining-critical-css-for-better-web-performance/)
    * 🛠 [Critical Path CSS Generator - Prioritize above the fold content :: SiteLocity](https://www.sitelocity.com/critical-path-css-generator)
    * 📖 [Reduce the size of the above-the-fold content](https://developers.google.com/speed/docs/insights/PrioritizeVisibleContent)

- [ ] **Embedded or inline CSS:** ![high] &#x202b;از inline CSS داخل `<body>` استفاده نکنید *(در HTTP/2 معتبر نیست)* 

    *&#x202b;چرا:*
    > &#x202b;اولین دلیل عادت خوب **جدا کردن طراحی از محتوا** است. این کار همچنین باعث می‌شود که قابلیت نگهداری و دسترسی در وبسایت شما بالا باشد. اما از دید کارایی، این عمل به سادگی باعث افزایش حجم صفحات شما می‌شود و زمان بارگزاری صفحه را افزایش می‌دهد.

    *&#x202b;چطور:*
    > &#x202b;همیشه از فایل‌های خارجی و یا قرار دادن کدهای CSS در درون بخش `<head>` استفاده کنید 

    * 📖 [Observe CSS Best Practices: Avoid CSS Inline Styles](https://www.lifewire.com/avoid-inline-styles-for-css-3466846)

- [ ] **Analyse stylesheets complexity:** ![high] &#x202b;بررسی استایل می‌تواند کمک کند تا مشکلات، موانع و قوانین تکراری را شناسایی کنید

    *&#x202b;چرا:*
    > &#x202b;برخی اوقات ممکن است خطاهایی را در فایل‌های CSS خود پیدا کنید. بررسی این فایل‌ها و رفع مشکلات موجود در آن‌ها باعث می‌شود که فایل‌های CSS شما سریع‌تر بارگزاری شوند

    *&#x202b;چطور:*
    > &#x202b;CSSهای شما باید سازماندهی شوند؛ این عمل با پیش پردازشگرهای CSS امکان پذیر است. لینک تعدادی از ابزارهای آنلاین در زیر قرار دارند که می‌توانید از آن‌ها برای بررسی و تصحیح کدهای خود استفاده کنید.

    * 🛠 [TestMyCSS | Optimize and Check CSS Performance](http://www.testmycss.com/)
    * 🛠 [CSS Stats](https://cssstats.com/)
    * 🛠 [macbre/analyze-css: CSS selectors complexity and performance analyzer](https://github.com/macbre/analyze-css)
    * 🛠 [Project Wallace](https://www.projectwallace.com/) is like CSS Stats but stores stats over time so you can track your changes

**[⬆ &#x202b;برگشت به بالا](#جدول-محتوا)**

## فونت ها

![fonts]

* 📖 [A Book Apart, Webfont Handbook](https://abookapart.com/products/webfont-handbook)

- [ ] **Webfont formats:** ![medium] &#x202b;شما باید از فرمت WOFF2 در پروژه وب یا اپلیکیشن خود استفاده کنید

    *&#x202b;چرا:*
    > &#x202b;طبق گفته گوگل، نسخه دوم فرمت فشرده وب فونت WOFF به طور میانگین 30% حجم کمتری نسبت به نسخه اول آن دارد. بهتر است که از WOFF 2.0  استفاده کرده و سپس از WOFF 1.0 و TTF به عنوان فرمت‌های پشتیبان در مرورگرهای قدیمی بهره ببرید.

    *&#x202b;چگونه:*
    > &#x202b;پیش از خرید فونت جدید اطمینان حاصل کنید که نسخه WOFF2 در اختیار شما قرار گیرد. اگر شما از یک فونت رایگان استفاده می‌کنید، می‌توانید از سایت‌هایی که فرمت‌های مورد نیاز شما را تولید می‌کنند کمک بگیرید. 

    * 📖 [WOFF 2.0 – Learn more about the next generation Web Font Format and convert TTF to WOFF2](https://gist.github.com/sergejmueller/cf6b4f2133bcb3e2f64a)
    * 🛠 [Create Your Own @font-face Kits » Font Squirrel](https://www.fontsquirrel.com/tools/webfont-generator)
    * 🛠 [IcoMoon App - Icon Font, SVG, PDF & PNG Generator](https://icomoon.io/app/)
    * 📖 [Using @font-face | CSS-Tricks](https://css-tricks.com/snippets/css/using-font-face/?ref=frontendchecklist)
    * 📖 [Can I use... WOFF2](https://caniuse.com/#feat=woff2)

- [ ] **Use `preconnect` to load your fonts faster:** ![medium] &#x202b;برای بارگزاری سریع فونت‌هایی که خارج از سرور شما قرار دارند از قابلیت `preconnect` استفاده کنید

    ```html
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    ```

    *&#x202b;چرا:*
    > &#x202b;زمانی که شما به وبسایتی مراجعه می‌کنید، مرورگر شما نیاز دارد که بداند سایت در کدام سرور میزبانی می‌شود تا بتوانید به آن سرور متصل شود. مرورگر شما مجبور است که به یک سرور DNS متصل گردد و تا پیش از دریافت منابع (فونت‌ها، فایل‌های CSS  و ...) منتظر بماند تا جستجوی مکان سرور شما کامل شود. تکنیک‌های Prefetch و Preconnect به مرورگر اجازه می‌دهند که اطلاعات DNS را جلوتر جستجو کند و شروع به ایجاد یک ارتباط TCP با سروری نماید که فونت‌های شما بر روی آن میزبانی می‌شوند. این کار باعث افزایش کارایی می‌شود چرا که زمانی که مرورگر در حال خواندن فایل CSS شماست و متوجه می‌شود که نیاز به اتصال به یک سرور خارجی برای بارگزاری فونت‌ها دارد، موارد مربوط به DNS از قبل انجام شده و این مورد باعث افزایش سرعت دریافت فونت‌ها می‌شود.

    *&#x202b;چگونه:*
    > - &#x202b;قبل از استفاده از تکنیک prefetch، از webpagetest برای بررسی سایت خود استفاده کنید <br>
    > - &#x202b;در گزارش تولید شده، به دنبال بخشی باشید که جستجوی DNS در آن قرار دارد و به هاست‌هایی که باید متصل شود اشاره می‌کند. <br>
    > - &#x202b;در بخش `<head>` از تکنیک prefetch برای وب فونت‌های خود استفاده کنید و در نهایت هاست‌های اشاره شده را نیز preconnect کنید.

    * 📖 [Faster Google Fonts with Preconnect - CDN Planet](https://www.cdnplanet.com/blog/faster-google-webfonts-preconnect/)
    * 📖 [Make Your Site Faster with Preconnect Hints | Viget](https://www.viget.com/articles/make-your-site-faster-with-preconnect-hints/)
    * 📖 [Ultimate Guide to Browser Hints: Preload, Prefetch, and Preconnect - MachMetrics Speed Blog](https://www.machmetrics.com/speed-blog/guide-to-browser-hints-preload-preconnect-prefetch/)
    * 📖 [A Comprehensive Guide to Font Loading Strategies—zachleat.com](https://www.zachleat.com/web/comprehensive-webfonts/#font-face)
    * 🛠 [typekit/webfontloader: Web Font Loader gives you added control when using linked fonts via @font-face.](https://github.com/typekit/webfontloader)

- [ ] **Webfont size:** ![medium] &#x202b;حجم مجموع فونت‌های استفاده نباید بیشتر از 300 کیلوبایت باشد

 * 📖 [Font Bytes - Page Weight](https://httparchive.org/reports/page-weight#bytesFont)

- [ ] **Prevent Flash or Invisible Text:** ![medium] &#x202b;پیش از بارگزاری فونت‌ها متن را نمایش دهید

 * 📖 [`font-display` for the Masses](https://css-tricks.com/font-display-masses/)
 * 📖 [CSS font-display: The Future of Font Rendering on the Web](https://www.sitepoint.com/css-font-display-future-font-rendering-web/)

**[⬆ &#x202b;برگشت به بالا](#جدول-محتوا)**

<h2 dir="rtl">تصاویر</h2>

![images]

 * 📖 [Image Bytes in 2018](https://httparchive.org/reports/page-weight#bytesImg)

* [ ] **Images optimization:** ![high] &#x202b;تصاویر شما بدون اینکه تاثیری در نمایش برای کاربر نهایی داشته باشند، باید بهینه و فشرده شوند

    *&#x202b;چرا:*
    > &#x202b;تصاویر بهینه سازی شده سریع‌تر در مرورگر بارگذاری می‌شوند و داده (اینترنتی) کمتری استفاده می‌کنند

    *&#x202b;چطور:*
    > &#x202b;- هر جا که امکان پذیر بود به جای تصاویر کوچک از افکت‌های CSS3 استفاده کنیپ <br>
    > &#x202b;- هر جا که ممکن بود از فونت‌ها به جای متون تصویری استفاده کنید <br>
    > &#x202b;- از SVG استفاده کنید <br>
    > &#x202b;- از ابزار استفاده کنید و سطح فشرده سازی آن را زیر ۸۵ قرار دهید

    * 📖 [Image Optimization | Web Fundamentals | Google Developers](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/image-optimization)
    * 📖 [Essential Image Optimization - An eBook by Addy Osmani](https://images.guide/)
    * 🛠 [TinyJPG – Compress JPEG images intelligently](https://tinyjpg.com/)
    * 🛠 [Kraken.io - Online Image Optimizer](https://kraken.io/web-interface)
    * 🛠 [Compressor.io - optimize and compress JPEG photos and PNG images](https://compressor.io/compress)
    * 🛠 [Cloudinary - Image Analysis Tool](https://webspeedtest.cloudinary.com)
    * 🛠 [ImageEngine - Image Webpage Loading Test](https://demo.imgeng.in)
    * 🛠 [SVGOMG - Optimize SVG vector graphics files](https://jakearchibald.github.io/svgomg/)


* [ ] **Images format:** ![high] &#x202b;فرمت مناسبی را برای تصاویر خود انتخاب کنید

    *&#x202b;چرا:*
    > &#x202b;برای اینکه مطمئن شوید که تصاویرتان، وبسایتتان را کند نمی‌کند، فرمتی را انتخاب کنید که مطابق تصویر شماست. اگر یک عکس داشتید، JPEG اغلب اوقات مناسب‌ترین انتخاب در مقایسه با PNG و GIF است. اما فراموش نکنید که نگاهی به فرمت‌های نسل بعدی بی‌اندازید که می‌توانند حجم فایل‌های شما را بیشتر کاهش دهند. هر فرمتی نقاط مثبت و منفی خود را دارد؛ این مورد به این دلیل مهم است که  بدانید بهترین انتخاب ممکن چیست. 

    *&#x202b;چطور:*
    > &#x202b;از ابزار [Lighthouse](https://developers.google.com/web/tools/lighthouse/) برای شناسایی اینکه کدام تصاویر می‌توانند از **فرمت‌های نسل بعدی** استفاده کنند، استفاده کنید. (مانند JPEG 2000 ،JPEG XR و یا WebP) <br>
    > &#x202b;فرمت‌های مختلف را با هم مقایسه کنید؛ برخی اوقات استفاده از PNG8 بسیار بهتر از PNG16 است و بعضی اوقات نه.

    * 📖 [Serve Images in Next-Gen Formats  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/lighthouse/audits/webp)
    * 📖 [What Is the Right Image Format for Your Website? — SitePoint](https://www.sitepoint.com/what-is-the-right-image-format-for-your-website/)
    * 📖 [PNG8 - The Clear Winner — SitePoint](https://www.sitepoint.com/png8-the-clear-winner/)
    * 📖 [8-bit vs 16-bit - What Color Depth You Should Use And Why It Matters - DIY Photography](https://www.diyphotography.net/8-bit-vs-16-bit-color-depth-use-matters/)

* [ ] **Use vector image vs raster/bitmap:** ![medium] &#x202b;هر زمان که ممکن بود، از تصاویر بُرداری به‌جای پیکسلی استفاده کنید

    *&#x202b;چرا:*
    > &#x202b; تصاویر برداری (مانند SVG) معمولا از فرمت‌های دیگر کم حجم‌تر هستند و تصاویر SVG واکنش‌گرا بوده و به خوبی مقیاس پذیر هستند. این نوع تصاویر می‌توانند متحرک شوند و به وسیله CSS در آن‌ها تغییراتی ایجاد داد (مانند تغییر رنگ) 

* [ ] **Images dimensions:** ![medium] &#x202b;اگر سایز تصویر مورد استفاده را می‌دانید، بر روی تگ `<img>` صفات `width` و `height` را تنظیم کنید

    *&#x202b;چرا:*
    > &#x202b;اگر طول و ارتفاع تصاویر مشخص شوند، فضایی که برای نمایش تصویر مورد نیاز است پیش از بارگذاری رزرو می‌شود. ولی بدون این صفات، مرورگر سایز تصاویر را نخواهد دانست و نمی‌تواند فضای مناسب را برای تصویر رزرو کند؛ و این کار باعث جابه‌جایی لایه‌ها در زمان بارگزاری تصاویر می‌شود.

* [ ] **Avoid using Base64 images:** ![medium] &#x202b;شما می‌توانید تصاویر کوچک را به base64 تبدیل کنید اما اینکار یک عادت خوب نیست

    * 📖 [Base64 Encoding & Performance, Part 1 and 2 by Harry Roberts](https://csswizardry.com/2017/02/base64-encoding-and-performance/)
    * 📖 [A closer look at Base64 image performance – The Page Not Found Blog](http://www.andygup.net/a-closer-look-at-base64-image-performance/)
    * 📖 [When to base64 encode images (and when not to) | David Calhoun](https://www.davidbcalhoun.com/2011/when-to-base64-encode-images-and-when-not-to/)
   * 📖 [Base64 encoding images for faster pages | Performance and seo factors](https://varvy.com/pagespeed/base64-images.html)

* [ ] **Lazy loading:** ![medium] &#x202b;تصاویری که در هنگام بارگذاری وبسایت در دید کاربر نیستند باید با استفاده از تکنیک lazy loading بارگذاری شوند

    *&#x202b;چرا:*
    > اینکار باعث بهبود زمان پاسخ در صفحه جاری می‌شود و در کنار آن، از بارگذاری تصاویر غیر ضروری که کاربر ممکن است به آن احتیاج نداشته باشد جلوگیری می‌کند.

    *&#x202b;چطور:*
    > &#x202b;- از ابزار [Lighthouse](https://developers.google.com/web/tools/lighthouse/) برای شناسایی **تصاویر خارج از دید** استفاده کنید. <br>
    > &#x202b;- از یک کتابخانه جاوا اسکریپت مانند مواردی که در پایین آورده شده‌اند برای بارگذاری تنبل (lazy load) تصاویر استفاده کنید. اطمینان حاصل کنید که این تکنینک را فقط برای تصاویر خارج از دید کاربر انجام دهید. <br>
    > &#x202b;- همچنین اطمینان حاصل کنید تصاویر جایگزین لود تنبل در زمان مناسب به کاربر نمایش داده شوند.

    * 🛠 [verlok/lazyload: GitHub](https://github.com/verlok/lazyload)
    * 🛠 [aFarkas/lazysizes: GitHub](https://github.com/aFarkas/lazysizes/)
    * 🛠 [mfranzke/loading-attribute-polyfill: GitHub](https://github.com/mfranzke/loading-attribute-polyfill/)
    * 📖 [Lazy Loading Images and Video  |  Web Fundamentals  |  Google Developers](https://developers.google.com/web/fundamentals/performance/lazy-loading-guidance/images-and-video/)
    * 📖 [5 Brilliant Ways to Lazy Load Images For Faster Page Loads - Dynamic Drive Blog](http://blog.dynamicdrive.com/5-brilliant-ways-to-lazy-load-images-for-faster-page-loads/)

* [ ] **Responsive images:** ![medium] &#x202b;اطمینان حاصل کنید که تصاویر متناسب با اندازه صفحه نمایش کاربر بکار برده شوند.

    *&#x202b;چرا:*
    > &#x202b;دستگاه‌های کوچک نیاز به تصاویر بزرگ‌تر از viewport خود نداردن. توصیه می‌شود که از چندین نسخه مختلف از یک عکس در سایزهای مختلف استفاده کنید.

    *&#x202b;چطور:*
    > &#x202b;اندازه‌های مختلف از تصویر را برای دستگاه‌هایی که مورد نظر شماست ایجاد کنید <br>
    > &#x202b; از صفت `srcset` و تگ `picture` برای نمایش نسخه‌های مختلف از تصویر خود استفاده کنید

     * 📖 [Responsive images - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

**[⬆ &#x202b;برگشت به بالا](#جدول-محتوا)**

<h2 dir="rtl">جاوا اسکریپت</h2>

![javascript]

- [ ] **JS Minification:** ![high] &#x202b; تمامی فایل‌های جاوا اسکریپت باید کوچک‌تر شده و کامنت‌ها، فضاهای خالی و خطوط اضافی در خروجی نهایی حذف شوند *(در HTTP/2 نیز معتبر است)*

    *&#x202b;چرا:*
    > &#x202b;حذف تمامی فضاهای خالی غیر ضروری، کامنت‌ها و خطوط اضافی باعث کاهش حجم فایل‌های جاوا اسکریپت شما شده و زمان بارگزاری صفحه وبسایت شما را سریع‌تر کرده و در نهایت حجم دانلود کمتری را برای کابران شما به دنبال دارد.

    *&#x202b;چطور:*
    > &#x202b;از ابزارهایی زیر که به شما پیشنهاد داده شده، برای کوچک کردن خودکار فایل‌های خود قبل و یا در حین تولید خروجی نهایی استفاده کنید.

    * 🛠 [uglify-js - npm](https://www.npmjs.com/package/uglify-js)
    * 🛠 [Online JavaScript Compressor](http://refresh-sf.com)
    * 📖 [Short read: How is HTTP/2 different? Should we still minify and concatenate?](https://scaleyourcode.com/blog/article/28)

* [ ] **No JavaScript inside:** ![medium] &#x202b; از قرار دادن کدهای جاوا اسکریپت در میان body خودداری کنید. تمامی کدهای جاوا اسکریپت خود را در فایل‌های خارجی دهید. شما همچنین می‌توانید کدهای جاوا اسکریپت را در تگ `<head>` و یا انتهای صفحه خود قرار دهید (قبل از `<body/>`)

    *&#x202b;چرا:*
    > &#x202b; قرار دادن کدها به صورت مستقیم داخل تگ `<body>` می‌تواند صفحه شما را به دلیل اینکه در زمان ایجاد DOM در حال بارگزاری هستد را کُند کند. بهترین گزینه می‌تواند استفاده از فایل‌های خارجی همراه با قابلیت `async` یا `defer` برای جلوگیری از مسدود کردن DOM می‌باشد. گزینه دیگر قرار دادن مقدار محدودی از کدهای جاوا اسکریپت داخل تگ `<head>` می‌باشد. بیشتر اوقات کدهای آمارگیری یا اسکریپت‌های کوچک باید پیش از ایجاد DOM بارگزاری شوند.

    *&#x202b;چگونه:*
    > &#x202b; اطمینان حاصل کنید که تمامی فایل‌های شما به وسیله قابلیت `defer` یا `async` بارگزاری شوند. همچنین در مورد کدهایی که در درون تگ `<head>` قرار می‌دهید با دقت تصمیم گیری کنید.

     * 📖 [11 Tips to Optimize JavaScript and Improve Website Loading Speeds](https://www.upwork.com/hiring/development/11-tips-to-optimize-javascript-and-improve-website-loading-speeds/)

* [ ] **Non-blocking JavaScript:** ![high] &#x202b; بارگزاری فایل‌های جاوا اسکریپت باید از طریق قابلیت `async` به صورت غیر همزمان و یا قابلیت `defer` به تعویق بی‌افتد.

    ```html
    <!-- Defer Attribute -->
    <script defer src="foo.js"></script>

    <!-- Async Attribute -->
    <script async src="foo.js"></script>
    ```

    *&#x202b;چرا:*
    > &#x202b;بارگزاری جاوا اسکریپت باعث مسدود سازی تجزیه (parse) سند اچ تی ام ال می‌شود؛ در نتیجه زمانی که تجزیه کننده به یک تگ `<script>` (که معمولا در داخل تگ `<head>` قرار دارد) می‌رسد، متوقف شده و اسکریپت را اجرا می‌کند. اگر اسکریپت‌های شما در ابتدای سند شما قرار دارند افزودن قابلیت `async` یا `defer` بسیار توصیه می‌شود در حالی که اگر این کدها در انتهای سند شما قرار دارند افزودن این قابلیت‌ها تاثیر چندانی ندارند. اما استفاده همیشگی از این قابلیت‌ها به عنوان یک عادت خوب برای جلوگیری از مشکلات کارایی به حساب می‌آید. 

    *&#x202b;چگونه:*
    > &#x202b; از قابلیت `async` (در صورتی که فایل شما وابسته به فایل‌های دیگر نیست) و قابلیت `defer` (اگر این فایل وابسته به فایل دیگر است) به عنوان یک صفت در تگ `<script>` استفده کنید. <br>
    > &#x202b;اگر اسکریپت کوچکی دارید، شاید بهتر باشد آن‌را به صورت داخلی (inline) بالای فایل‌های جاوا اسکریپت قرار دهید.

    * 📖 [Remove Render-Blocking JavaScript](https://developers.google.com/speed/docs/insights/BlockingJS)
    * 📖 [Defer loading JavaScript](https://varvy.com/pagespeed/defer-loading-javascript.html)

* [ ] **Optimized and updated JS libraries:** ![medium] &#x202b;تمامی کتابخانه‌های جاوا اسکریپت که در پروژ استفاده می‌شوند باید ضروری باشند (برای عملکردهای ساده ترجیحا از جاوا اسکریپت خام استفاده کنید)؛ و به آخرین نسخه آپدیت شده باشند. 

    *&#x202b;چرا:*
    > &#x202b;اکثر اوقات، نسخه‌های جدید همراه با بهینه سازی و رفع مشکلات امنیتی است. بهتر است که شما از بهینه‌ترین نسخه برای افزایش سرعت پروژه خود استفاده کنید و مطمئن شوید که وبسایت یا اپلیکیشن شما از نسخه‌های قدیمی استفاده نمی‌کنند.

    *&#x202b;چطور:*
    > &#x202b;- اگر پروژه شما از پکیج‌های NPM استفاده می‌کند، [npm-check](https://www.npmjs.com/package/npm-check) یک گزینه مناسب برای بروزرسانی کتابخانه‌های مورد استفاده شماست. <br>
    >  &#x202b;- [Greenkeeper](https://greenkeeper.io/) می‌تواند به صورت خودکار کتابخانه‌های شما را بررسی کند و هرگاه یک بروزرسانی در دسترس بود به شما پیشنهاد دهد.

    * 📖 [You may not need jQuery](http://youmightnotneedjquery.com/)
    * 📖 [Vanilla JavaScript for building powerful web applications](https://plainjs.com/)

- [ ] **Check dependencies size limit:** ![low] &#x202b;از کتابخانه‌های خارجی به طور هوشمندانه استفاده کنید؛ بیشتر اوقات شما می‌توانید از یک کتابخانه کوچک‌تر برای عملکرد مشابه بهره ببرید.

    *&#x202b;چرا:*
    > &#x202b; شما ممکن است مجبور به استفاده از یکی از 745 هزار پکیجی که در [npm](https://www.npmjs.com/) موجود است، شوید؛ اما شما نیاز دارید  که بهترین پکیجی که متناسب با نیاز شماست را استفاده کنید. برای مثال MomentJS یک کتابخانه فوق العاده با تعداد زیادی عملکرد است که ممکن است به کار شما نیاید و به همین دلیل است که Day.js ایجاد شده است؛ که حجم آن 2Kb در مقابل 16.4KB در نسخه gz است. 

    *&#x202b;چطور:*
    > &#x202b;همیشه مقایسه کنید و بهترین و کم حجم‌ترین کتابخانه متناسب با نیازهای خود را انتخاب کنید. شما همچنین می‌توانید از ابزاری مانند [npm trends](http://www.npmtrends.com/) برای مقایسه تعداد دانلودهای پکیج‌ها و یا [Bundlephobia](https://bundlephobia.com/) برای شناخت حجم پکیج‌های مورد نیاز، استفاده کنید. 

    * 🛠 [ai/size-limit: Prevent JS libraries bloat. If you accidentally add a massive dependency, Size Limit will throw an error.](https://github.com/ai/size-limit)
    * 🛠 [webpack-bundle-analyzer - npm](https://www.npmjs.com/package/webpack-bundle-analyzer)
    * 🛠 [js-dependency-viewer - npm](https://www.npmjs.com/package/js-dependency-viewer)
    * 📖 [Size Limit: Make the Web lighter — Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/size-limit-make-the-web-lighter)

- [ ] **JavaScript Profiling:** ![medium] &#x202b;مشکلات کارایی در فایل‌های جاوا اسکریپت (و سی‌اس‌اس) را بررسی کنید

    *&#x202b;چرا:*
    > &#x202b;پیچیدگی در کدهای جاوا اسکریپت می‌تواند کارایی زمان اجرا را کاهش دهد. شناسایی این مشکلات بالقوه برای دریافت بهترین تجربه کاربری ضروری است.

    *&#x202b;چطور:*
    > &#x202b;از ابزار Timeline موجود در ابزارهای توسعه دهنده کروم برای ارزیابی رویدادهای اسکریپت و پیدا کردن آن رویدادی که ممکن است اجرای آن طولانی باشد، استفاده کنید. 

     * 📖 [Speed Up JavaScript Execution  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/chrome-devtools/rendering-tools/js-execution)
    * 📖 [JavaScript Profiling With The Chrome Developer Tools — Smashing Magazine](https://www.smashingmagazine.com/2012/06/javascript-profiling-chrome-developer-tools/)
    * 📖 [How to Record Heap Snapshots  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/chrome-devtools/memory-problems/heap-snapshots)
    * 📖 [Chapter 22 - Profiling the Frontend - Blackfire](https://blackfire.io/docs/book/22-frontend-profiling)
    * 📖 [30 Tips To Improve Javascript Performance](http://www.monitis.com/blog/30-tips-to-improve-javascript-performance/)

- [ ] **Use of Service Workers:** ![medium] از سرویس ورکر در PWA به عنوان کش کردن داده‌ها و یا اجرای وظایف سنگین بدون تاثیر گذاشتن روی تجربه کاربری بهره ببرید
   
    * 📖 [Service Workers: an Introduction  |  Web Fundamentals  |  Google Developers](https://developers.google.com/web/fundamentals/primers/service-workers/)
    * 📖 [Measuring the Real-world Performance Impact of Service Workers  |  Web  |  Google Developers](https://developers.google.com/web/showcase/2016/service-worker-perf)
    * 📖 [What Are Service Workers and How They Help Improve Performance](https://www.keycdn.com/blog/service-workers/)
    * 📹 [How does a service worker work? - YouTube](https://www.youtube.com/watch?v=__xAtWgfzvc)

**[⬆ &#x202b;برگشت به بالا](#جدول-محتوا)**

<h2 dir="rtl">سرور</h2>

![server-side]

- [ ] **Your website is using HTTPS:** ![high]

    *&#x202b;چرا:*
    > &#x202b;HTTPS نه تنها برای فروشگاه‌های اینترنتی، بلکه برای تمامی وبسایت‌هایی است که در حال تبادل اطلاعات هستند. داده‌هایی که توسط یک کاربر به اشتراک گذاشته شده‌اند یا داده‌هایی که در یک موجودیت خارجی به اشتراک گذاشته شده‌اند. مرورگرهای مدرن امروزه عملکرد محدودی در قبال وبسایت‌های غیر امن دارند. برای مثال: مکان یابی کاربر، ارسال نوتفیکیشن و سرویس ورکرها در سایت‌هایی که از HTTPS استفاده نمی‌کنند، کار نمی‌کند. امروزه فعال کردن SSL خیلی راحت‌تر از گذشته است. (با تشکر از [Let's Encrypt](https://letsencrypt.org/) رایگان نیز هست). 

 * 📖 [Why Use HTTPS? | Cloudflare](https://www.cloudflare.com/learning/security/why-use-https/)
 * 📖 [Enabling HTTPS Without Sacrificing Your Web Performance - Moz](https://moz.com/blog/enabling-https-without-sacrificing-web-performance)
 * 📖 [How HTTPS Affects Website Performance](https://wp-rocket.me/blog/https-affects-website-performance/)
 * 📖 [HTTP versus HTTPS versus HTTP2 - The real story | Tune The Web](https://www.tunetheweb.com/blog/http-versus-https-versus-http2/)
 * 📖 [HTTP vs HTTPS — Test them both yourself](https://www.httpvshttps.com/)

- [ ] **Page weight < 1500 KB (ideally < 500 KB):** ![high] &#x202b;تا جایی که می‌توانید حجم صفحه و فایل‌های موجود در آن را کاهش دهید.

    *&#x202b;چرا:*
    > &#x202b;در حالت ایده‌آل شما باید حجم صفحه خود را کمتر از 500 کیلوبایت نگه دارید؛ گرچه وضعیت وبسایت‌ها نشان می‌دهد که میانگین صفحات موجود در وب 1500  کیلوبایت حجم دارند (حتی روی موبایل). با توجه به کاربران هدف، وضعیت اتصال شبکه و دستگاه، مهم است تا جایی که امکان دارد مجموع حجم صفحه را کاهش دهید تا تجربه کاربری بهتری داشته باشید.

    *&#x202b;چطور:*
    > &#x202b;تمامی قواینین موجود در این چک لیست به شما کمک می‌کند تا حد امکان حجم کدها و منابع خود را کاهش دهید.

    * 📖 [Page Weight](https://httparchive.org/reports/page-weight#bytesTotal)
    * 🛠 [What Does My Site Cost?](https://whatdoesmysitecost.com/)
    * 🛠 [web - Measure full page size in Chrome DevTools - Stack Overflow](https://stackoverflow.com/questions/38239980/measure-full-page-size-in-chrome-devtools)

- [ ] **Page load times < 3 seconds:** ![high] تا جایی که ممکن است زمان بارگزاری صفحه را کاهش دهید تا محتوا سریع‌تر به دست کاربر برسد.

    *&#x202b;چرا:*
    > &#x202b;هر چقدر اپلیکیشن یا وبسایت شما سریع‌تر باشد، شانس رهایی کمتر می‌شود. به زبان دیگر شما شانس کمتری برای از دست دادن کاربر دارید. بررسی‌های زیادی برای اثبات این مورد انجام گرفته است.

    *&#x202b;چطور:*
    > &#x202b;از ابزارهای آنلاین مانند [Page Speed Insight](https://developers.google.com/speed/pagespeed/insights/) یا [WebPageTest](https://www.webpagetest.org/) برای بررسی صفحات و این لیست کارایی فرانت‌اند جهت بهبود سرعت بارگزاری استفاده کنید. 

    * 🛠 [Compare your mobile site speed](https://www.thinkwithgoogle.com/feature/mobile/)
    * 🛠 [Test Your Mobile Website Speed and Performance - Think With Google](https://testmysite.thinkwithgoogle.com/intl/en-us)
    * 📖 [Average Page Load Times for 2018 - How does yours compare? - MachMetrics Speed Blog](https://www.machmetrics.com/speed-blog/average-page-load-times-websites-2018/)

- [ ] **Time To First Byte < 1.3 seconds:** ![high] &#x202b;هر چقدر که می‌توانید مدت زمانی که مرورگر منتظر دریافت پاسخ از سمت سرور است را کاهش دهید

    * 📖 [What is Waiting (TTFB) in DevTools, and what to do about it](https://scaleyourcode.com/blog/article/27)
    * 📖 [Monitoring your servers with free tools is easy](https://scaleyourcode.com/blog/article/7)
    * 📖 [Time to First Byte (TTFB)](https://varvy.com/pagespeed/ttfb.html)
    * 🛠 [Global latency testing tool](https://latency.apex.sh)

* [ ] **Cookie size:** ![medium] &#x202b;اگر شما از کوکی‌ها استفاده می‌کنید، دقت کنید که حجم هر کوکی از 4096 بایت بیشتر نشود و هر دامنه بیشتر از 20 کوکی نداشته باشد

    *&#x202b;چرا:*
    > کوکی‌ها در حال تبادل بین کاربر و سرور از طریق HTTP header هستند. مهم است که حجم کوکی‌ها را تا جایی که امکان دارد کاهش دهید تا روی زمان پاسخ به کاربر حداقل تاثیر را بگذارد.

    *&#x202b;چطور:*
    > &#x202b;کوکی‌های غیر ضروری را حذف کنید.

    * 📖 [Cookie specification: RFC 6265](https://tools.ietf.org/html/rfc6265)
    * 📖 [Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
    * 🛠 [Browser Cookie Limits](http://browsercookielimits.squawky.net/)
    * 📖 [Website Performance: Cookies Don't Taste So Good - Monitis Blog](http://www.monitis.com/blog/website-performance-cookies-dont-taste-so-good/)
    * 📖 [Google's Web Performance Best Practices #3: Minimize Request Overhead - GlobalDots Blog](https://www.globaldots.com/googles-web-performance-best-practices-3-minimize-request-overhead/)

- [ ] **Minimizing HTTP requests:** ![high] &#x202b;اطمینان حاصل کنید که هر فایل درخواستی برای وبسایت یا اپلیکیشن شما ضروری است.

 * 📖 [Combine external CSS](https://varvy.com/pagespeed/combine-external-css.html)
 * 📖 [Combine external JavaScript](https://varvy.com/pagespeed/combine-external-javascript.html)

- [ ] **Use a CDN to deliver your assets:** ![medium] &#x202b;از CDN برای رساندن سریع محتوای خود به سرتاسر جهان استفاده کنید

 * 📖 [10 Tips to Optimize CDN Performance - CDN Planet](https://www.cdnplanet.com/blog/10-tips-optimize-cdn-performance/)
 * 📖 [HTTP Caching  |  Web Fundamentals  |  Google Developers](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching)

- [ ] **Serve files from the same protocol:** ![high] &#x202b;برای مثال اگر از HTTPS استفاده می‌کنید، نباید فایل‌های موجود در صفحه را از طریق HTTP فراخوانی کمید. اگر وبسایت شما HTTPS است فایل‌های موجود در صفحه نیز باید از همین پروتکل دریافت شوند.

- [ ] **Serve reachable files:** ![high] &#x202b;از درخواست دادن به صفحات و فایل‌های ناموجود خودداری کنید (خطای 404)
 * 📖 [How to avoid bad requests](https://varvy.com/pagespeed/avoid-bad-requests.html)

- [ ] **Set HTTP cache headers properly:** ![high] &#x202b;از HTTP header جهت کاهش ارسال درخواست و دریافت پاسخ بین سرور و کاربر استفاده کنید.
 * 📖 [Using cache-control for browser caching](https://varvy.com/pagespeed/cache-control.html)

- [ ] **GZIP / Brotli compression is enabled:** ![high] &#x202b;از یک متد فشرده سازی مانند Gzip یا Brotli جهت کاهش حجم فایل‌های خود استفاده کنید. هر چقدر حجم فایل‌ها کمتر باشد، کاربر آن‌ها را سریع‌تر دریافت کرده و در نتیجه کارایی بهتر می‌شود.

 * 🛠 [Check GZIP compression](https://checkgzipcompression.com/)
 * 🛠 [Check Brotli Compression](https://tools.keycdn.com/brotli-test)
 * 📖 [Can I use... Brotli](https://caniuse.com/#feat=brotli)

**[⬆ &#x202b;برگشت به بالا](#جدول-محتوا)**

---
## Performances and JS Frameworks

### Angular
 * 📖 [Angular Performance Checklist](https://github.com/mgechev/angular-performance-checklist)

### React

 * 📖 [Optimizing Performance - React](https://reactjs.org/docs/optimizing-performance.html)
 * 📖 [React image manipulation | Cloudinary](https://cloudinary.com/documentation/react_image_manipulation)
 * 📖 [Debugging React performance with React 16 and Chrome Devtools.](https://building.calibreapp.com/debugging-react-performance-with-react-16-and-chrome-devtools-c90698a522ad)
  * 📖 [Build Performant - React](https://web.dev/react/)

### Vue
 * 📖 [Vue - Useful Links|Style Guide and Performance](https://learn-vuejs.github.io/vue-patterns/useful-links/)

## Performances and CMS

### WordPress

* 🛠 [Test Your Website Speed | WordPress Hosting by @WPEngine](https://wpengine.com/speed-tool/)

#### Articles

 * 📖 [19 Tips to Speed Up WordPress Performance (Updated)](https://www.wpbeginner.com/wordpress-performance-speed/)
 * 📖 [Speed Up Your WordPress - How to Save Images Optimized for Web](https://www.wpbeginner.com/beginners-guide/speed-wordpress-save-images-optimized-web/)

#### Plugins recommended

* 🛠 [Caching Plugin for WordPress - Speed up your website with WP Rocket](https://wp-rocket.me/)
* 🛠 [WP-Sweep | WordPress.org](https://wordpress.org/plugins/wp-sweep/)
* 🛠 [Imagify Image Optimizer | WordPress.org](https://wordpress.org/plugins/imagify/)

---

## Translations

The Front-End Performance Checklist wants to also be available in other languages! Don't hesitate to submit your contribution!

* 🇵🇹 Portuguese: [fernandofawkes/Front-End-Performance-Checklist](https://github.com/fernandofawkes/Front-End-Performance-Checklist)
* 🇨🇳 Chinese: [JohnsenZhou/Front-End-Performance-Checklist](https://github.com/JohnsenZhou/Front-End-Performance-Checklist)
* 🇷🇺 Russian: [lex111/Front-End-Performance-Checklist](https://github.com/lex111/Front-End-Performance-Checklist)
* 🇫🇷 French: [WilliamDASILVA/Front-End-Performance-Checklist](https://github.com/WilliamDASILVA/Front-End-Performance-Checklist)
* 🇰🇷 Korean: [ParkSB/Front-End-Performance-Checklist](https://github.com/ParkSB/Front-End-Performance-Checklist)
* 🇪🇸 Spanish: [dagerzuga/Front-End-Performance-Checklist](https://github.com/dagerzuga/Front-End-Performance-Checklist)
* 🇻🇮 Vietnamese : [huynhan147/Front-End-Performance-Checklist](https://github.com/huynhan147/FrontEnd-Performance-Checklist)
* 🇯🇵 Japanese: [GameWith/Front-End-Performance-Checklist](https://github.com/GameWith/Front-End-Performance-Checklist)
* 🇵🇱 Polish: [mbiesiad/Front-End-Performance-Checklist](https://github.com/mbiesiad/Front-End-Performance-Checklist)

## &#x202b;همکاری

**Open an issue or a pull request to suggest changes or additions.**

## Support

If you have any question or suggestion, don't hesitate to use Discord or Twitter:

* [Chat on Discord](https://discord.gg/btHQRkm)
* [Facebook](https://www.facebook.com/frontendchecklist/)
* [Twitter](https://twitter.com/thedaviddias)

## Author

**Build with ❤️ by [David Dias](https://github.com/thedaviddias)

## Contributors

This project exists thanks to all the people who contribute. [[Contribute]](.github/CONTRIBUTING.md).
<a href="https://github.com/thedaviddias/Front-End-Performance-Checklist/graphs/contributors">
    <img src="https://opencollective.com/front-end-checklist/contributors.svg?width=890" />
</a>


## Backers

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/front-end-checklist#backer)]

<a href="https://opencollective.com/front-end-checklist#backers" target="_blank"><img src="https://opencollective.com/front-end-checklist/backers.svg?width=890"></a>


## Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/front-end-checklist#sponsor)]

<a href="https://opencollective.com/front-end-checklist/sponsor/0/website" target="_blank"><img src="https://opencollective.com/front-end-checklist/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/front-end-checklist/sponsor/1/website" target="_blank"><img src="https://opencollective.com/front-end-checklist/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/front-end-checklist/sponsor/2/website" target="_blank"><img src="https://opencollective.com/front-end-checklist/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/front-end-checklist/sponsor/3/website" target="_blank"><img src="https://opencollective.com/front-end-checklist/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/front-end-checklist/sponsor/4/website" target="_blank"><img src="https://opencollective.com/front-end-checklist/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/front-end-checklist/sponsor/5/website" target="_blank"><img src="https://opencollective.com/front-end-checklist/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/front-end-checklist/sponsor/6/website" target="_blank"><img src="https://opencollective.com/front-end-checklist/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/front-end-checklist/sponsor/7/website" target="_blank"><img src="https://opencollective.com/front-end-checklist/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/front-end-checklist/sponsor/8/website" target="_blank"><img src="https://opencollective.com/front-end-checklist/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/front-end-checklist/sponsor/9/website" target="_blank"><img src="https://opencollective.com/front-end-checklist/sponsor/9/avatar.svg"></a>

## License

[MIT](LICENSE)

All icons are provided by [Icons8](https://icons8.com/)

**[⬆ back to top](#table-of-contents)**

[logo]: images/logo-front-end-performance-checklist.jpg
[html]: images/html.png
[css]: images/css.png
[fonts]: images/fonts.png
[images]: images/images.png
[javascript]: images/javascript.png
[server-side]: images/server-side.png

[low]: images/priority/low.svg
[medium]: images/priority/medium.svg
[high]: images/priority/high.svg
