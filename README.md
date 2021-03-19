<h1 align="center" dir="rtl">
<br>
  <a href="https://github.com/thedaviddias/Front-End-Performance-Checklist"><img src="https://raw.githubusercontent.com/thedaviddias/Front-End-Performance-Checklist/master/images/logo-front-end-performance-checklist.jpg" alt="Front-End Performance Checklist" width="170"></a>
  <br>
  <br>
  Front-End Performance Checklist  
  <br>
  چک لیست کارایی در فرانت‌اند
  <br>
</h1>

<h4 align="center" dir="rtl">🎮 تنها چک لیست مربوط به مباحث کارایی در فرانت‌اند که سریع تر از بقیه اجرا می‌شه.</h4>
<p align="center" dir="rtl">یک قانون ساده: "با کارایی در ذهنتون طراحی و برنامه‌نویسی کنین"</p>

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
  <a href="#نحوه-استفاده">نحوه استفاده</a> • <a href="#contributing">Contributing</a>
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

<p align="center">
    <span>Other Checklists:</span>
    <br>
  🗂 <a href="https://github.com/thedaviddias/Front-End-Checklist#---------front-end-checklist-">Front-End Checklist</a> • 💎 <a href="https://github.com/thedaviddias/Front-End-Design-Checklist#front-end-design-checklist">Front-End Design Checklist</a>
</p>

<h2 dir="rtl">جدول محتوا</h2>

<ol dir="rtl">
  
<li>
  
  **[اچ تی ام ال](#اچ-تی-ام-ال)**

</li>
<li>
  
  **[سی اس اس](#سی-اس-اس)**
  
</li>
<li>
  
  **[فونت ها](#فونت-ها)**

</li>
<li>
  
  **[تصاویر](#تصاویر)**

</li>
<li>
  
  **[جاوا اسکریپت](#javascript)**
  
</li>
<li>
  
  **[سرور](#server) (در دست اجرا)**

</li>
<li>
  
  **[فریم‌ورک‌های جاوا اسکریپت](#performances-and-js-frameworks) (در دست اجرا)**
 
</li>

</ol>

<h2 dir="rtl">معرفی</h2>

<p dir="rtl">
کارایی موضوع گسترده‌ای است و همیشه مربوط به "بک‌اند" و "ادمین" نیست؛ بلکه "فرانت‌اند" هم در این زمینه مسئولیت‌هایی دارد. چک لیست کارایی فرانت‌اند، یک لیست کامل از مواردی است که شما باید به عنوان یک توسعه دهنده فرانت‌اند، آن‌ها را بررسی کنید و یا حداقل از وجود این موارد آگاه شوید و این موارد را در پروژه‌های خود اعمال کنید. (پروژه‌های شخصی و حرفه‌ای).
</p>

<h3 dir="rtl">نحوه استفاده</h3>

<p dir="rtl">
  برای هر یک از قوانین، یک بند وجود دارد که توضیح می‌دهد <em>چرا</em> این قانون مهم است و <em>چگونه</em> می‌توانید آن را رفع کنید. برای اطلاعات بیشتر نیز به سراغ لینک‌های بروید که به عنوان 🛠 ابزار، 📖 مقاله و یا 📹 رسانه علامت گذاری شده‌اند و می‌توانند مکمل این چک لیست باشند.
</p>
<p dir="rtl">
تمامی موارد در <strong>چک لیست کارایی فرانت‌اند</strong> برای رسیدن به بالاترین امتیاز کارایی ضروری و مهم هستند اما شما شما می‌توانید یک شاخص را ببنید که به شما در الویت بندی قوانین (برای بررسی و اعمال) کمک کند. در مجموع 3 شاخص برای الویت وجود دارند: 
</p>

<ul dir="rtl">
  
<li>
  
![Low][low] به این معنی است که این مورد الویت **کم** دارد.
  
</li>
<li>

![Medium][medium] به این معنی است که این مورد الویت **متوسط** دارد. شما نباید از این موارد صرف نظر کنید.

</li>
<li>

![High][high] به این معنی است که این مورد الویت **بالا** دارد. شما نمی‌توانید در استفاده از دنبال کردن از این مورد خودداری کنید و باید اصلاحات توصیه شده را پیاده سازی کنید.

</li>

</ul>

### Performance tools

List of the tools you can use to test or monitor your website or application:

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


### References

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

<h2 dir="rtl">اچ تی ام ال</h2>

![html]

- [ ] **Minified HTML:** ![medium] &#x202b;صفحه HTML شما کوچک‌تر شده و کامنت‌ها، فضاهای خالی و خطوط اضافی از خروجی نهایی حذف خواهند شد

    *چرا&#x202b;:*
    > &#x202b;حذف فضاهای خالی، کامنت‌ها و صفات غیر ضروری باعث کاهش اندازه صفحه HTML شما شده و سرعت بارگزاری صفحه شما را افزایش می‌دهد و مشخصا دانلود سبک‌تری را برای کاربران به ارمغان می‌آورد.

    *&#x202b;چگونه:*
    > &#x202b;بیشتر فریم ورک‌ها، پلاگین‌ها و ابزارهایی دارند که وظیفه آن‌ها کوچک کردن صفحات HTML است. شما می‌توانید از ماژول‌های بسیار زیاد NPM که اینکار را به صورت خودکار انجام می‌دهند استفاده کنید.
    * 🛠 [HTML minifier | Minify Code](http://minifycode.com/html-minifier/)
    * 🛠 [Online HTML Compressor](http://refresh-sf.com)
    * 📖 [Experimenting with HTML minifier — Perfection Kills](http://perfectionkills.com/experimenting-with-html-minifier/#use_short_doctype)
   
- [ ] **Place CSS tags always before JavaScript tags:** ![high] &#x202b;اطمینان حاصل کنید که سی اس اس پیش از کدهای جاوا اسکریپت قرار گیرد

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
    > &#x202b;قرار دادن سی اس اس پیش از جاوا اسکریپت، قابلیت دانلود بهتر و موازی را فراهم می‌کند که باعث افزایش سرعت در زمان رندر مرورگر می‌شود.

    *&#x202b;چگونه:*
    > &#x202b;اطمینان حاصل کنید `<link>` و `<style>` در قسمت `<head>` همیشه قبل از `<script>` قرار داشته باشند.

    * 📖 [&#x202b;مرتب سازی استایل‌ها و اسکریپت‌ها برای افزایش سرعت صفحه](https://varvy.com/pagespeed/style-script-order.html)

- [ ] **Minimize the number of iframes:** ![high] &#x202b;تنها در صورتی از iframe استفاده کنید که قادر به استفاده از روش دیگری نباشید. تلاش کنید که تا حد امکان از iframe استفاده نکنید

- [ ] **Pre-load optimization with prefetch, dns-prefetch and prerender:** ![low] &#x202b;مرورگرهای معروف می‌توانند با استفاده از تگ `<link>` و صفت `rel` با مقادیر مشخص، آدرس‌های خاصی را پیش بارگذاری کنند

    *&#x202b;چرا:*
    > &#x202b; امکان Prefetching به مرورگر اجازه می‌دهد تا به طور نامحسوس منابع ضروری را که در آینده برای نشان دادن محتوا به کاربر مورد استفاده قرار می‌گیرند را دریافت کند. مرورگر قادر است این منابع را در کش خود ذخیره کند و باعث افزایش سرعت بارگذاری صفحه شود. زمانی که بارگذاری صفحه جاری به پایان رسید و پردازنده بیکار شد، مرورگر شروع به دانلود این منابع می‌کند؛ و زمانی که کاربر به یک لینک مشخص مراجعه می‌کند (در حالی که منابع آن از قبل دریافت شده) محتوا سریعا برای کاربر نمایش داده خواهد شد. 

    *&#x202b;چطور:*
    > &#x202b;مطمئن شوید که از تگ `<link>` به درستی در بخش `<head>` استفاده کنید.

    * 📖 [&#x202b;Prefetching چیست و چرا از آن استفاده می‌شود](https://www.keycdn.com/support/prefetching)
    * 📖 [Prefetching, preloading, prebrowsing](https://css-tricks.com/prefetching-preloading-prebrowsing/)
    * 📖 [&#x202b;Preload ،Prefetch و Preconnect چیستند؟](https://www.keycdn.com/blog/resource-hints)

**[⬆ &#x202b;برگشت به بالا](#جدول-محتوا)**

<h2 dir="rtl">سی اس اس</h2>

![css]

- [ ] **Minification:** ![high] &#x202b;تمامی فایل‌های CSS کوچک‌تر شده و کامنت‌ها، فضاهای خالی و خطوط اضافی از خروجی نهایی حذف خواهند شد

    *&#x202b;چرا:*
    > &#x202b;زمانی که فایل‌های CSS کوچک تر می‌شوند، محتوا سریع‌تر بارگذاری شده و داده کمتری برای دانلود به سمت کاربر ارسال می‌شود. کوچک کردن فایل‌های CSS در خروجی نهایی بسیار مهم است. این مورد هم به نفع کاربر و هم به نفع کسب و کاری است که قصد دارد هزینه پهنای باند و استفاده از منابع را کاهش دهد.

    *&#x202b;چگونه:*
    > &#x202b;از ابزارهایی استفاده کنید که فایل‌های مورد نظر را به صورت خودکار در زمان تولید خروجی نهایی و یا پیش از آن کوچک کنند.

    * 🛠 [cssnano: &#x202b;یک کوچک کننده ماژولار که در اکوسیستم PostCSS اجرا می‌شود](https://cssnano.co/)
    * 🛠 [CSS Minfier](https://goonlinetools.com/css-minifier/)
    * 🛠 [@neutrinojs/style-minify - npm](https://www.npmjs.com/package/@neutrinojs/style-minify)
    * 🛠 [Online CSS Compressor](http://refresh-sf.com)


- [ ] **Concatenation:** ![medium] &#x202b;فایل‌های CSS در یک فایل ادغام شوند *(ممکن است برای HTTP/2 معتبر نباشد)*.

    ```html

    <!-- توصیه نمی‌شود -->
    <link rel="stylesheet" href="foo.css"/>
    <link rel="stylesheet" href="bar.css"/>

    <!-- توصیه می‌شود -->
    <link rel="stylesheet" href="foobar.css"/>
    ```

    *&#x202b;چرا:*
    > &#x202b;اگر شما هنوز هم از HTTP/1 استفاده می‌کنید، ممکن است نیاز باشد تا فایل‌ها را ادغام کنید. این مورد زمانی که شما از HTTP/2 استفاده می‌کنید کمتر معتبر است. (نیاز به تست و بررسی)

    *&#x202b;چگونه:*
    > &#x202b;- از ابزارهای آنلاین یا هر پلاگین دیگری که در زمان تولید خروجی نهایی و یا پیش از آن فایل‌های شما را ادغام می‌کنند استفاده کنید. <br>
    > &#x202b;- البته اطمینان حاصل کنید که این ادغام باعث خرابی در پروژه شما نشود.

    * 📖 [HTTP: Optimizing Application Delivery - High Performance Browser Networking (O'Reilly)](https://hpbn.co/optimizing-application-delivery/#optimizing-for-http2)
    * 📖 [Performance Best Practices in the HTTP/2 Era](https://deliciousbrains.com/performance-best-practices-http2/)

- [ ] **Non-blocking:** ![high] &#x202b;نیاز است فایل‌های سی‌اس‌اس non-blocking باشند تا از معطل شدن بارگذاری DOM جلوگیری شود

    ```html
    <link rel="preload" href="global.min.css" as="style" onload="this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="global.min.css"></noscript>
    ```

    *&#x202b;چرا:*
    > &#x202b;فایل‌های CSS می‌توانند از بارگذاری صفحه جلوگیری کنند و رندر صفحه شما را به تاخیر بی‌اندازند. با استفاده از `preload` می‌توان بارگذاری فایل‌های سی‌اس‌اس را پیش از نمایش محتوا آغاز کرد.

    *&#x202b;چطور:*
    > &#x202b;تنها با افزودن صفت `rel` را همراه با مقدار `preload` و اضافه کردن `as="style"` به تگ `<link>`.

    * 🛠 [loadCSS by filament group](https://github.com/filamentgroup/loadCSS)
    * 📖 [&#x202b;مثال‌های از پیش بارگذاری CSS با استفاده از loadCSS](https://gist.github.com/thedaviddias/c24763b82b9991e53928e66a0bafc9bf)
    * 📖 [&#x202b;پیش‌بارگذاری محتوا با استفاده از rel="preload"](https://developer.mozilla.org/en-US/docs/Web/HTML/Preloading_content)
    * 📖 [Preload: &#x202b;برای چی خوبه؟](https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/)

- [ ] **Unused CSS:** ![medium] &#x202b;قوانین بی‌استفاده را حذف کنید

    *&#x202b;چرا:*
    > &#x202b;حذف قوانین بی‌استفاده در CSS می‌تواند باعث کاهش حجم فایل‌ها شود و سپس سرعت برگذاری فایل‌ها بیشتر کند.

    *&#x202b;چطور:*
    > &#x202b;⚠️ همیشه فریم‌ورک‌های مورد استفاده‌تان را بررسی کنید تا کدهای اضافی نداشته باشند. بیشتر اوقات شما به تمامی قوانین موجود در این فریم‌ورک‌ها احتیاج نخواهید داشت.

    * 🛠 [UnCSS Online](https://uncss-online.com/)
    * 🛠 [PurifyCSS](https://github.com/purifycss/purifycss)
    * 🛠 [PurgeCSS](https://github.com/FullHuman/purgecss)
    * 🛠 [Chrome DevTools Coverage](https://developers.google.com/web/updates/2017/04/devtools-release-notes#coverage)

* [ ] **CSS Critical:** ![high] &#x202b;سی‌اس‌اس‌های ضروری ("critical" یا "above the fold") شامل تمامی قوانین‌های سی‌اس‌اس هستند که برای نمایش بخش بالای صفحه (در زمان بارگذاری) مورد نیاز است. این قوانین پیش از خطوط تعریف فایل‌های سی‌اس‌اس در داخل تگ `<style></style>` قرار میگیرند. 

    *&#x202b;چرا:*
    > &#x202b;استفاده از سی‌اس‌اس‌های ضروری باعث افزایش سرعت در رندر صفحات می‌شود و تعداد درخواست‌ها به سرور را کاهش می‌دهد.

    *&#x202b;چگونه:*
    > &#x202b;سی‌اس‌اس‌های ضروری را  با استفاده از ابزار آنلاین و یا پلاگین‌های موجود (مثلا ابزاری که ادی عثمانی توسعه داده است) تولید کنید.

    * 📖 [&#x202b;سی‌اس‌اس‌های ضروری را بفهمید](https://www.smashingmagazine.com/2015/08/understanding-critical-css/)
    * 🛠 [Critical by Addy Osmani on GitHub](https://github.com/addyosmani/critical) automates this.
    * 📖 [&#x202b;سی‌اس‌اس‌های ضروری برای برای بهتر شدن کارایی وبسایت](https://gomakethings.com/inlining-critical-css-for-better-web-performance/)
    * 🛠 [Critical Path CSS Generator - Prioritize above the fold content :: SiteLocity](https://www.sitelocity.com/critical-path-css-generator)
    * 📖 [&#x202b;حجم منابع برای بارگذاری محتوای بالای صفحه را کاهش دهید](https://developers.google.com/speed/docs/insights/PrioritizeVisibleContent)

- [ ] **Embedded or inline CSS:** ![high] &#x202b;از inline CSS داخل `<body>` استفاده نکنید *(در HTTP/2 معتبر نیست)* 

    *&#x202b;چرا:*
    > &#x202b;اولین دلیل عادت خوب **جدا کردن طراحی از محتوا** است. این کار همچنین باعث می‌شود که قابلیت نگهداری و دسترسی در وبسایت شما بالا باشد. اما از بُعد کارایی، این عمل به سادگی باعث افزایش حجم صفحات شما می‌شود و زمان بارگذاری را افزایش می‌دهد.

    *&#x202b;چطور:*
    > &#x202b;همیشه از external stylesheets و یا embed CSS در درون تگ `<head>` استفاده کنید (و بقیه قوانین کارایی در بخش سی‌اس‌اس را دنبال کنید) 

    * 📖 [&#x202b;عادات خوب در CSS: از inline CSS دوری کنید](https://www.lifewire.com/avoid-inline-styles-for-css-3466846)

- [ ] **Analyse stylesheets complexity:** ![high] &#x202b;بررسی استایل می‌تواند کمک کند تا مشکلات، موانع و قوانین تکراری را شناسایی کنید

    *&#x202b;چرا:*
    > &#x202b;برخی اوقات شما ممکن است خطاهایی را در فایل‌های سی‌اس‌ای خود پیدا کنید. بررسی این فایل‌ها و حذف این پیچیدگی‌ها باعث می‌شود که فایل‌های CSS شما سریع‌تر شوند (چون مرورگر آن‌ها را سریع‌تر می‌خواند)

    *&#x202b;چطور:*
    > &#x202b;CSSهای شما باید سازماندهی شوند؛ که این عمل با پیش پردازشگرهای CSS امکان پذیر است. تعدادی از ابزارهای آنلاین در زیر وجود دارند که می‌توانید از آن‌ها برای بررسی و تصحیح کدهای خود استفاده کنید.

    * 🛠 [TestMyCSS | &#x202b;بهینه‌سازی و بررسی کارایی CSS](http://www.testmycss.com/)
    * 🛠 [CSS Stats](https://cssstats.com/)
    * 🛠 [macbre/analyze-css: &#x202b;بررسی کننده کارایی و پیچیدگی قوانین CSS](https://github.com/macbre/analyze-css)
    * 🛠 [Project Wallace](https://www.projectwallace.com/) is like CSS Stats but stores stats over time so you can track your changes

**[⬆ &#x202b;برگشت به بالا](#جدول-محتوا)**

<h2 dir="rtl">فونت ها</h2>

![fonts]

* 📖 [&#x202b;کتابچه راهنمای وب فونت](https://abookapart.com/products/webfont-handbook)

- [ ] **Webfont formats:** ![medium] &#x202b;شما باید از فرمت WOFF2 در پروژه وب یا اپلیکیشن خود استفاده کنید

    *&#x202b;چرا:*
    > &#x202b;طبق گفته گوگل، نسخه دوم فرمت فشرده وب فونت WOFF به طور میانگین 30% حجم کمتری نسبت به نسخه اول WOFF دارد. خوب است که از WOFF 2.0  استفاده کرده و سپس از WOFF 1.0 و TTF به عنوان پشتیبانی از مرورگرهای قدیمی بهره ببرید.

    *&#x202b;چگونه:*
    > &#x202b;پیش از خرید فونت جدید اطمینان حاصل کنید که نسخه WOFF2 در اختیار شما قرار گیرد. اگر شما از یک فونت رایگان استفاده می‌کنید، می‌توانید از سایت‌هایی استفاده کنید که فرمت‌های مورد نیاز شما را تولید می‌کنند. 

    * 📖 [WOFF 2.0 – &#x202b;درباره فرمت نسل بعدی وب فونت‌ها بیشتر بدانید و TTF را به WOFF2 تبدیل کنید](https://gist.github.com/sergejmueller/cf6b4f2133bcb3e2f64a)
    * 🛠 [Font Squirrel - &#x202b;@font-face خود را بسازید](https://www.fontsquirrel.com/tools/webfont-generator)
    * 🛠 [IcoMoon App - Icon Font, SVG, PDF & PNG Generator](https://icomoon.io/app/)
    * 📖 [Using @font-face | CSS-Tricks](https://css-tricks.com/snippets/css/using-font-face/?ref=frontendchecklist)
    * 📖 [Can I use... WOFF2](https://caniuse.com/#feat=woff2)

- [ ] **Use `preconnect` to load your fonts faster:** ![medium]

    ```html
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    ```

    *&#x202b;چرا:*
    > &#x202b;زمانی که شما به وبسایتی مراجعه می‌کنید، دستگاه شما نیاز دارد که بداند سایت شما کجاست و به کدام سرور متصل شود. مرورگر شما مجبور است که به یک سرور DNS متصل گردد و تا پیش از دریافت منابع (فونت‌ها، فایل‌های CSS  و ...) منتظر بماند تا جستجو کامل شود. تکنیک‌های Prefetch و Preconnect به مرورگر اجازه می‌دهند که اطلاعات DNS را جستجو کند و شروع به ایجاد یک ارتباط TCP با سروری نماید که فونت‌های شما بر روی آن میزبانی می‌شوند. این کار باعث افزایش کارایی می‌شود چرا که زمانی که مرورگر در حال خواندن فایل CSS شماست و متوجه می‌شود که نیاز به اتصال به یک سرور برای فونت‌ها دارد، موارد مربوط به DNS از قبل انجام شده و این مورد باعث افزایش سرعت دریافت فونت‌ها می‌شود.

    *&#x202b;چگونه:*
    > &#x202b;- قبل از استفاده از تکنیک prefetch، از webpagetest برای بررسی سایت خود استفاده کنید <br>
    > &#x202b;- در گزارش به دنبال بخشی باشید که جستجو DNS در آن قرار دارد و به هاست‌هایی که باید متصل شود اشاره می‌کند. <br>
    > &#x202b;- در بخش `<head>` از تکنیک prefetch برای وب فونت‌های خود استفاده کنید و در نهایت هاست‌های اشاره شده را نیز preconnect کنید.

    * 📖 [&#x202b;فونت‌های گوگل را با preconnect سریع‌تر کنید - CDN Planet](https://www.cdnplanet.com/blog/faster-google-webfonts-preconnect/)
    * 📖 [&#x202b;سایت خود را با preconnect سریع‌تر کنید | Viget](https://www.viget.com/articles/make-your-site-faster-with-preconnect-hints/)
    * 📖 [&#x202b;راهنمای کامل برای نکات مرورگر: Preload ،Prefetch و Preconnect - MachMetrics Speed Blog](https://www.machmetrics.com/speed-blog/guide-to-browser-hints-preload-preconnect-prefetch/)
    * 📖 [A&#x202b;راهنمای جامع استراتژی‌های بارگذاری فونت—zachleat.com](https://www.zachleat.com/web/comprehensive-webfonts/#font-face)
    * 🛠 [typekit/webfontloader: &#x202b;این ابزار کنترل بیشتری را برای فونت‌های موجود در @font-face به شما می‌دهد.](https://github.com/typekit/webfontloader)

- [ ] **Webfont size:** ![medium] &#x202b;حجم فونت‌ها نباید بیشتر از 300 کیلوبایت باشد (مجموع فونت‌های مورد استفاده)

 * 📖 [&#x202b;بایت فونت - حجم صفحه](https://httparchive.org/reports/page-weight#bytesFont)

- [ ] **Prevent Flash or Invisible Text:** ![medium] &#x202b;پیش از بارگذاری فونت‌ها متن را نمایش دهید

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

**[⬆ back to top](#table-of-contents)**

## JavaScript

![javascript]

- [ ] **JS Minification:** ![high] All JavaScript files are minified, comments, white spaces and new lines are removed from production files *(still valid if using HTTP/2)*.

    *Why:*
    > Removing all unnecessary spaces, comments and break will reduce the size of your JavaScript files and speed up your site's page load times and obviously lighten the download for your user.

    *How:*
    > ⁃ Use the tools suggested below to minify your files automatically before or during your build or your deployment.

    * 🛠 [uglify-js - npm](https://www.npmjs.com/package/uglify-js)
    * 🛠 [Online JavaScript Compressor](http://refresh-sf.com)
    * 📖 [Short read: How is HTTP/2 different? Should we still minify and concatenate?](https://scaleyourcode.com/blog/article/28)

* [ ] **No JavaScript inside:** ![medium] *(Only valid for website)* Avoid having multiple JavaScript codes embedded in the middle of your body. Regroup your JavaScript code inside external files or eventually in the `<head>` or at the end of your page (before `</body>`).

    *Why:*
    > Placing JavaScript embedded code directly in your `<body>` can slow down your page because it loads while the DOM is being built. The best option is to use external files with `async` or `defer` to avoid blocking the DOM. Another option is to place some scripts inside your `<head>`. Most of the time analytics code or small script that need to load before the DOM gets to main processing.

    *How:*
    > Ensure that all your files are loaded using `async` or `defer` and decide wisely the code that you will need to inject in your `<head>`.

     * 📖 [11 Tips to Optimize JavaScript and Improve Website Loading Speeds](https://www.upwork.com/hiring/development/11-tips-to-optimize-javascript-and-improve-website-loading-speeds/)

* [ ] **Non-blocking JavaScript:** ![high] JavaScript files are loaded asynchronously using `async` or deferred using `defer` attribute.

    ```html
    <!-- Defer Attribute -->
    <script defer src="foo.js"></script>

    <!-- Async Attribute -->
    <script async src="foo.js"></script>
    ```

    *Why:*
    > JavaScript blocks the normal parsing of the HTML document, so when the parser reaches a `<script>` tag (particularly is inside the `<head>`), it stops to fetch and run it. Adding `async` or `defer` are highly recommended if your scripts are placed in the top of your page but less valuable if just before your `</body>` tag. But it's a good practice to always use these attributes to avoid any performance issue.

    *How:*
    > ⁃ Add `async` (if the script don't rely on other scripts) or `defer` (if the script relies upon or relied upon by an async script) as an attribute to your script tag. <br>
    ⁃ If you have small scripts, maybe use inline script place above async scripts.

    * 📖 [Remove Render-Blocking JavaScript](https://developers.google.com/speed/docs/insights/BlockingJS)
    * 📖 [Defer loading JavaScript](https://varvy.com/pagespeed/defer-loading-javascript.html)

* [ ] **Optimized and updated JS libraries:** ![medium] All JavaScript libraries used in your project are necessary (prefer Vanilla JavaScript for simple functionalities), updated to their latest version and don't overwhelm your JavaScript with unnecessary methods.

    *Why:*
    > Most of the time, new versions come with optimization and security fix. You should use the most optimized code to speed up your project and ensure that you'll not slow down your website or app without outdated plugin.

    *How:*
    > If your project use NPM packages, [npm-check](https://www.npmjs.com/package/npm-check) is a pretty interesting library to upgrade / update your libraries.
    > [Greenkeeper](https://greenkeeper.io/) can automatically look for your dependencies and suggest an update every time a new version is out.

    * 📖 [You may not need jQuery](http://youmightnotneedjquery.com/)
    * 📖 [Vanilla JavaScript for building powerful web applications](https://plainjs.com/)

- [ ] **Check dependencies size limit:** ![low] Ensure to use wisely external libraries, most of the time, you can use a lighter library for a same functionality.

    *Why:*
    > You may be tempted to use one of the 745 000 packages you can find on [npm](https://www.npmjs.com/), but you need to choose the best package for your needs. For example, MomentJS is an awesome library but with a lot of methods you may never use, that's why Day.js was created. It's just 2kB vs 16.4kB gz for Moment.

    *How:*
    > Always compare and choose the best and lighter library for your needs. You can also use tools like [npm trends](http://www.npmtrends.com/) to compare NPM package downloads counts or [Bundlephobia](https://bundlephobia.com/) to know the size of your dependencies.

    * 🛠 [ai/size-limit: Prevent JS libraries bloat. If you accidentally add a massive dependency, Size Limit will throw an error.](https://github.com/ai/size-limit)
    * 🛠 [webpack-bundle-analyzer - npm](https://www.npmjs.com/package/webpack-bundle-analyzer)
    * 🛠 [js-dependency-viewer - npm](https://www.npmjs.com/package/js-dependency-viewer)
    * 📖 [Size Limit: Make the Web lighter — Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/size-limit-make-the-web-lighter)

- [ ] **JavaScript Profiling:** ![medium] Check for performance problems in your JavaScript files (and CSS too).

    *Why:*
    > JavaScript complexity can slow down runtime performance. Identifying these possible issues are essential to offer the smoothest user experience.

    *How:*
    > Use the Timeline tool in the Chrome Developer Tool to evaluate scripts events and found the one that may take too much time.

     * 📖 [Speed Up JavaScript Execution  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/chrome-devtools/rendering-tools/js-execution)
    * 📖 [JavaScript Profiling With The Chrome Developer Tools — Smashing Magazine](https://www.smashingmagazine.com/2012/06/javascript-profiling-chrome-developer-tools/)
    * 📖 [How to Record Heap Snapshots  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/chrome-devtools/memory-problems/heap-snapshots)
    * 📖 [Chapter 22 - Profiling the Frontend - Blackfire](https://blackfire.io/docs/book/22-frontend-profiling)
    * 📖 [30 Tips To Improve Javascript Performance](http://www.monitis.com/blog/30-tips-to-improve-javascript-performance/)

- [ ] **Use of Service Workers:** ![medium] You are using Service Workers in your PWA to cache data or execute possible heavy tasks without impacting the user experience of your application.
   
    * 📖 [Service Workers: an Introduction  |  Web Fundamentals  |  Google Developers](https://developers.google.com/web/fundamentals/primers/service-workers/)
    * 📖 [Measuring the Real-world Performance Impact of Service Workers  |  Web  |  Google Developers](https://developers.google.com/web/showcase/2016/service-worker-perf)
    * 📖 [What Are Service Workers and How They Help Improve Performance](https://www.keycdn.com/blog/service-workers/)
    * 📹 [How does a service worker work? - YouTube](https://www.youtube.com/watch?v=__xAtWgfzvc)

**[⬆ back to top](#table-of-contents)**

## Server

![server-side]

- [ ] **Your website is using HTTPS:** ![high]

    *Why:*
    > HTTPS is not only for ecommerce websites, but for all websites that are exchanging data. Data shared by a user or data shared to an external entity. Modern browsers today limit functionalities for sites that are not secure. For example: geolocation, push notifications and service workers don't work if your instance is not using HTTPS. And today is much more easy to setup a project with an SSL certificate than it was before (and for free, thanks to [Let's Encrypt](https://letsencrypt.org/)).

 * 📖 [Why Use HTTPS? | Cloudflare](https://www.cloudflare.com/learning/security/why-use-https/)
 * 📖 [Enabling HTTPS Without Sacrificing Your Web Performance - Moz](https://moz.com/blog/enabling-https-without-sacrificing-web-performance)
 * 📖 [How HTTPS Affects Website Performance](https://wp-rocket.me/blog/https-affects-website-performance/)
 * 📖 [HTTP versus HTTPS versus HTTP2 - The real story | Tune The Web](https://www.tunetheweb.com/blog/http-versus-https-versus-http2/)
 * 📖 [HTTP vs HTTPS — Test them both yourself](https://www.httpvshttps.com/)

- [ ] **Page weight < 1500 KB (ideally < 500 KB):** ![high] Reduce the size of your page + resources as much as you can.

    *Why:*
    > Ideally you should try to target < 500 KB but the state of web shows that the median of Kilobytes is around 1500 KB (even on mobile). Depending on your target users, network connection, devices, it's important to reduce as much as possible your total Kilobytes to have the best user experience possible.

    *How:*
    > ⁃ All the rules inside the Front-End Performance Checklist will help you to reduce as much as possible your resources and your code.

    * 📖 [Page Weight](https://httparchive.org/reports/page-weight#bytesTotal)
    * 🛠 [What Does My Site Cost?](https://whatdoesmysitecost.com/)
    * 🛠 [web - Measure full page size in Chrome DevTools - Stack Overflow](https://stackoverflow.com/questions/38239980/measure-full-page-size-in-chrome-devtools)

- [ ] **Page load times < 3 seconds:** ![high] Reduce as much as possible your page load times to quickly deliver your content to your users.

    *Why:*
    > Faster your website or app is, less you have probability of bounce increases, in other terms you have less chances to lose your user or future client. Enough researches on the subject prove that point.

    *How:*
    > Use online tools like [Page Speed Insight](https://developers.google.com/speed/pagespeed/insights/) or [WebPageTest](https://www.webpagetest.org/) to analyze what could be slowing you down and use the Front-End Performance Checklist to improve your load times.

    * 🛠 [Compare your mobile site speed](https://www.thinkwithgoogle.com/feature/mobile/)
    * 🛠 [Test Your Mobile Website Speed and Performance - Think With Google](https://testmysite.thinkwithgoogle.com/intl/en-us)
    * 📖 [Average Page Load Times for 2018 - How does yours compare? - MachMetrics Speed Blog](https://www.machmetrics.com/speed-blog/average-page-load-times-websites-2018/)

- [ ] **Time To First Byte < 1.3 seconds:** ![high] Reduce as much as you can the time your browser waits before receiving data.

    * 📖 [What is Waiting (TTFB) in DevTools, and what to do about it](https://scaleyourcode.com/blog/article/27)
    * 📖 [Monitoring your servers with free tools is easy](https://scaleyourcode.com/blog/article/7)
    * 📖 [Time to First Byte (TTFB)](https://varvy.com/pagespeed/ttfb.html)
    * 🛠 [Global latency testing tool](https://latency.apex.sh)

* [ ] **Cookie size:** ![medium] If you are using cookies, be sure each cookie doesn't exceed 4096 bytes and your domain name doesn't have more than 20 cookies.

    *Why:*
    > Cookies are exchanged in the HTTP headers between web servers and browsers. It's important to keep the size of cookies as low as possible to minimize the impact on the user's response time.

    *How:*
    > Eliminate unnecessary cookies.

    * 📖 [Cookie specification: RFC 6265](https://tools.ietf.org/html/rfc6265)
    * 📖 [Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
    * 🛠 [Browser Cookie Limits](http://browsercookielimits.squawky.net/)
    * 📖 [Website Performance: Cookies Don't Taste So Good - Monitis Blog](http://www.monitis.com/blog/website-performance-cookies-dont-taste-so-good/)
    * 📖 [Google's Web Performance Best Practices #3: Minimize Request Overhead - GlobalDots Blog](https://www.globaldots.com/googles-web-performance-best-practices-3-minimize-request-overhead/)

- [ ] **Minimizing HTTP requests:** ![high] Always ensure that every file requested are essential for your website or application.
 * 📖 [Combine external CSS](https://varvy.com/pagespeed/combine-external-css.html)
 * 📖 [Combine external JavaScript](https://varvy.com/pagespeed/combine-external-javascript.html)

- [ ] **Use a CDN to deliver your assets:** ![medium] Use a CDN to deliver faster your content over the world.

 * 📖 [10 Tips to Optimize CDN Performance - CDN Planet](https://www.cdnplanet.com/blog/10-tips-optimize-cdn-performance/)
 * 📖 [HTTP Caching  |  Web Fundamentals  |  Google Developers](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching)

- [ ] **Serve files from the same protocol:** ![high] Avoid having your website serving files coming from source using HTTP on your website which is using HTTPS for example. If your website is using HTTPS, external files should come from the same protocol.

- [ ] **Serve reachable files:** ![high] Avoid requesting unreachable files (404).
 * 📖 [How to avoid bad requests](https://varvy.com/pagespeed/avoid-bad-requests.html)

- [ ] **Set HTTP cache headers properly:** ![high] Set HTTP headers to avoid expensive number of roundtrips between your browser and the server.
 * 📖 [Using cache-control for browser caching](https://varvy.com/pagespeed/cache-control.html)

- [ ] **GZIP / Brotli compression is enabled:** ![high] Use a compression method such as Gzip or Brotli to reduce the size of your JavaScript files. With a smaller sizes file, users will be able to download the asset faster, resulting in improved performance.

 * 🛠 [Check GZIP compression](https://checkgzipcompression.com/)
 * 🛠 [Check Brotli Compression](https://tools.keycdn.com/brotli-test)
 * 📖 [Can I use... Brotli](https://caniuse.com/#feat=brotli)

**[⬆ back to top](#table-of-contents)**

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

## Contributing

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
