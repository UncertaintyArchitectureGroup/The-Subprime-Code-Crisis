# Аудит доказів, розміщення джерел і мови звіту — 2026-10-20

Owner: [#53](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/53). Governance implementation: [#47](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/47), [#52](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/52), [PR #56](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/pull/56).

## Висновок і межі роботи

Корисне ядро репозиторію — розрізнення швидкості створення коду й результатів delivery, а також потреба вимірювати downstream-ефекти. Наявна доказова база не підтримує сильнішу універсальну тезу, що AI вже сповільнює всю індустрію, неминуче руйнує якість або веде до системної кризи. Частина досліджень показує позитивні результати, зокрема downstream-зростання. Це потрібно зберегти в центральному аргументі, а не лише у вступному застереженні.

Рекомендована теза:

> AI coding tools can increase coding activity and improve some delivery outcomes. These gains vary by task, tool, population, and operating model. When additional work exceeds downstream verification and delivery capacity, local acceleration may produce queues, rework, or risk. This report examines that conditional mechanism and the evidence needed to distinguish it from successful adaptation.

Це **аудит і план виправлення**, а не завершені Flow A–D для всіх джерел. Канонічний текст report, briefs і source states цим PR не виправляються та не підвищуються до `Verified`. Висновки нижче — підстава для окремих source-oriented briefs, інтеграційних PR та незалежної перевірки. Наявний статус NBER описує перевірку 2026-07-27; він не означає підтвердження всіх нових висновків цього аудиту.

Перевірено весь поточний `report/` (10 розділів), README/діаграму, REFERENCES, усі чотири protocols та їх індекс, SOURCES, три наявні briefs, terminology/provenance surfaces і правила роботи. Охоплено **25 зареєстрованих джерел**: 8 empirical, 10 documentary, 6 secondary/context, 1 methodology. У реєстрі: 18 `Registered / Not started`, 3 `Reviewed brief / In progress`, 3 `Needs re-review / Needs re-verification`, 1 `Reviewed brief / Verified`. Три briefs охоплюють сім source IDs. Окремо виявлено незареєстровані або недостатньо ідентифіковані джерела.

«Охоплено» означає перевірку наявного використання та доступних оригіналів/обмежень доступу. Це не означає повний доступ до кожного gated документа, відтворення досліджень із raw data чи підтвердження кожного історичного стану вебсторінки. Для Goldratt повний текст/сторінки конкретного видання не перевірені; для GitClear quality повний gated report не отриманий; для TechnoDiaries доступний вступ; для частини LinkedIn provenance є обмеження. Ці прогалини залишаються відкритими.

## Зафіксований стан і спосіб перевірки

- Subprime main: `06fdd63b332fd4efe27462dbbd648119c3f96ce8`.
- Початковий head PR #56: `8a9637f7b1937b594ed0cf0bac66974f9bde3468`. Research content у цьому PR не відрізнявся від main; номери рядків нижче стосуються цього стану. Heading + фрагмент є стійким locator після зсуву рядків.
- Авторський сайт: `oborskyivitalii/oborskyivitalii`, main commit `82b57b8948c6c30143213b846ee2848d06f8d200` (перевірено branch API).
- Дата доступу до зовнішніх сторінок: 2026-10-20. Дата доступу не замінює дату публікації, версію paper або historical snapshot.
- NBER перевірявся за наданим користувачем `01-w35275.pdf`, May 2026; SHA-256 `edf1a41a6e4e4cf562571b5fac79eac07693281f88d460a81ee9f8ce1a1c65bb`. Повний copyrighted PDF у репозиторій не додається. Офіційний URL залишається в bibliography.
- Оригінали: versioned arXiv HTML, METR, first-party GitClear, McKinsey 2025, SEC/annual reports, Google engineering book, Menlo/CloudZero. Documentary/secondary review незалежно виконано другим агентом; його межі й результат нижче.
- Для кожного source ID нижче розділено: що підтримується, помилки/невизначеність, поточне місце, рекомендоване місце. Окремі claim IDs дозволяють закривати конкретні виправлення без втрати контексту.

## Що переноситься з авторського сайту

| Практика | Реалізація в Subprime | Для чого |
| --- | --- | --- |
| Issue зберігає intent і acceptance criteria | Stable `AC-*`, PR/commit `Refs #N`, незакриті criteria залишаються відкритими | Не втрачати мету між чатами, PR і rebase |
| Датована коротка передача контексту | `governance/memory.md`, п'ять секцій, максимум 120 рядків | Швидкий вхід із перевіркою актуального GitHub state |
| RI дає маршрути, не дослідницьку істину | `inventory`, `context-for-task`, source brief/current-use, scoped instructions, advisory check routes | Знайти owner і потрібні перевірки перед редагуванням |
| Freshness включає asset bytes | SHA-256 для всіх admitted files, явні size/exclusion bounds | Зміна binary не може непомітно залишити projection «свіжою» |
| Перевірка конкретного evidence і версії | Per-occurrence numeric/inference/placement review, exact source locator | Не підмінювати валідатором перевірку змісту |
| Професійна критика | Умовні механізми, альтернативи, спростовувані прогнози; без непідтверджених мотивів | Зберегти сильну аргументацію без звинувачень |

Не перенесено site release controllers, browser profiles, повний path catalog, semantic graph і окремий acceptance engine. Поточний обсяг Subprime цього не потребує. RI не перевіряє правдивість джерел, виконання команд, CI reachability або поточний стан issues/PR. Existing trusted-base gate залишається окремим.

## Матриця всіх 25 зареєстрованих джерел

Позначення місць: **R1/R2/R3** = відповідні файли `report/01_the_illusion.md`, `02_broken_mechanics.md`, `03_the_aftermath.md`; **Ch** = номер розділу. Для кожного рядка також перевірено наявність у `evidence/SOURCES.md`, `REFERENCES.md` та evidence index; конкретний brief вказано, якщо він існує. Загальні згадки класів у README не замінюють source-specific trace.

| ID / оригінал | Поточне використання | Результат перевірки | Рішення про місце |
| --- | --- | --- | --- |
| **P-2026-01 — NBER w35275**, supplied May PDF, abstract, Fig. 1, Table 5, §§7–9 | R1 Ch1; R2 Ch7; README Crisis Map; primary brief | Headline +180% commits / +50% projects / +30% releases відповідає abstract. Це cumulative stack, не окремий async release effect; Table 5 async releases не оцінює. 0.25 — model-calibrated. Marketplace outcome — early engagement proxies, не весь customer value. | Головний синтез у Ch1; у Ch7 короткий cross-reference + межі механізму. Зберегти позитивне зростання релізів. C09–C10. |
| **P-2025-01 — [METR early-2025 RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)** | R1 Ch1, refs; README evidence map | 16 developers, 246 familiar OSS tasks; +19% time, а не універсальна втрата продуктивності. Очікування і self-estimate відділити від elapsed time. | Залишити в порівняльній таблиці Ch1 з tool/date/task scope; додати окремий temporal update 2026. C02. |
| **P-2025-02 — [METR task horizon](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)** | R1 Ch3; R2 Ch5; refs обох | 50% — визначення конкретного fitted horizon. Це не загальна ймовірність помилки frontier agent. Поточний графік і March 2025 paper змішані; 7-month horizon trend не доводить doubling code volume. | Один measurement box у Ch5: versioned benchmark, reliability level, human-time estimation; у Ch3 лише cross-reference. C18. |
| **P-2025-03 — [Xu v3](https://arxiv.org/html/2510.10165v3)** | R1 Ch1/Ch4, refs; README | 2,755 Microsoft-owned OSS repos, 1,699 contributors; не 10,000 enterprise developers. Core — верхній квартиль попередньої commit activity, не seniority. +43.5% — нижній квартиль; +6.5% review count, не години. Project gains не «зникають» після авторської поправки репо. | Ch1 — окремий observational study; Ch4 — лише обмежена підтримка redistribution hypothesis, не replication METR. C03–C04. |
| **P-2026-02 — [Agarwal v2](https://arxiv.org/html/2601.13597v2)** | R1 Ch1/Ch4, repeated conclusions/refs; README | +18% warnings / +39% cognitive complexity — repository-month measures у studied adoption comparison. Не per-feature debt, functional correctness або measured human cognitive load. Agent-first/IDE-first heterogeneity і позитивні activity outcomes не губити. | Quality/proxy subsection Ch1; Ch4 посилається на межі, не переносить коефіцієнт у модель review effort. C05. |
| **P-2023-01 — [Peng v1](https://arxiv.org/html/2302.06590v1)** | R1 Ch1 positive evidence + refs; README | 95 randomized (45/50), 70 completers (35/35), не 196. 55.8% — менший completion time у bounded HTTP-server task; denominator/completion condition потрібні. | Поряд із METR у центральній таблиці heterogeneous effects, не відступ перед запереченням. C01. |
| **P-2025-04 — [GitClear quality](https://www.gitclear.com/ai_assistant_code_quality_2025_research)** | R1 Ch1/refs; R2 Ch6; README | Landing page доступна; повний report gated. 211M changed lines, Jan 2020–Dec 2024; не спільна вибірка з productivity report. Moved lines, copy/paste lines і clone-containing commits — різні одиниці. | Окремий code-change/proxy box Ch1; усі 8×/10× та context-window claims вважати непідтвердженими до exact table/page. Ch6 — без universal degradation inference. C06. |
| **P-2025-05 — [GitClear productivity](https://www.gitclear.com/research/ai_tool_impact_on_developer_productive_output_from_2022_to_2025)** | R1 Ch1 числа фактично під quality link; R1 Ch4; R2 Ch5 | Original embedded report: +131.1% mean lines, +76.3% median lines; medians +6.8/+6.1/+14.1 для трьох methods дають авторські +9.0%. Два числа в репо дають 10.1%. Composite не є causal AI productivity / net delivery. | Окремо від quality dataset. Retain observable measures, прибрати synthesized «net gain» і universal doubling. C07–C08. |
| **D-2019-01 — [Software Engineering at Google](https://abseil.io/resources/swe-book)** | R1 Ch2; refs | Book published March **2020**. [Ch23](https://abseil.io/resources/swe-book/html/ch23.html) підтримує >4B daily test cases; не exact 4.2B, $1B TAP cost або $1–3B platform cost. Critique не замінює людську перевірку. | Engineering practice context у Ch2; вилучити monetary inference без джерел. Stable ID можна зберегти з corrected bibliography. C12. |
| **D-2024-01 — [Alphabet 2024 10-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204425000014/goog-20241231.htm)** | R1 Ch2 table + refs | R&D **$49.326B**, а $45.427B належить 2023; purchases PPE $52.535B. Total corporate figures не budget AI-code verification. | Якщо залишати — contextual appendix з accounting lines/period; не доказ multiplier. Guidance2025 окремо від actual2024. C11. |
| **D-2024-02 — [Meta 2024 report](https://www.sec.gov/Archives/edgar/data/1326801/000132680125000043/meta-12312024x10kars.htm)** | R1 Ch2 table + generic IR link | R&D **$43.873B**, не $44.4B. Capex definition потрібно узгодити: PPE purchases проти total capex including finance lease principal. | Той самий appendix; exact filing замість IR homepage; не виділяти всю R&D як enabling infrastructure. C11. |
| **D-2024-03 — [Microsoft FY2024 report](https://www.microsoft.com/investor/reports/ar24/index.html)** | R1 Ch2 table + refs | $29.510B R&D / $44.477B additions PPE збігаються; FY ends June30. CY run-rate extrapolation і 2025 investment guidance не actual comparable CY capex. | Appendix із FY label й окремими guidance sources або прибрати нерелевантний макрофінансовий блок. C11. |
| **D-2025-05 — Nick Vigier** | `TERMINOLOGY_AND_ATTRIBUTION.md`; terminology brief; refs | Незалежний reviewer підтвердив поточний original article і дату 2025-09-16 для terminology use. Не empirical delivery study. | Залишити лише attribution/history. C29. |
| **D-2025-06 — Igor Światowski** | Ті самі attribution surfaces | Indexed listing з назвою є; direct page 999, related post 404. Дату Dec16 цього разу незалежно не відтворено. | Зберегти dated prior observation і access gap; потрібен accessible dated original/archive. C29. |
| **D-2026-04 — Richard Ewing, multiple surfaces** | Attribution, terminology brief, refs | Old CareerWin URL redirect на renamed article; old concept404; old blog renamed. Current concept self-claims April2025, origin link не підтверджує дату. Beehiiv має стару phrase, без видимої дати. | Separate observed-page/date records у provenance; не реконструювати незбережену історію та мотиви. C29. |
| **D-2026-05 — [DOU Jan5](https://dou.ua/forums/topic/57244/)** | README; attribution; project brief; refs | Стаття і Jan8 comments підтримують dated precursor і refinement. Авторська публікація не незалежне підтвердження її емпіричних тверджень. | Поточне history placement доречне. C30. |
| **D-2026-06 — [GitHub metadata](https://api.github.com/repos/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis)** | README; attribution; project brief; refs | `created_at=2026-02-06T17:16:44Z` підтверджено. Current public visibility не доводить visibility в момент створення. | У chronology «repository object created». Поточна DOU-сторінка з датою Feb10 містить посилання; без архівного snapshot історичний момент public opening незалежно не встановлено. C30. |
| **D-2026-07 — [DOU Feb10](https://dou.ua/forums/topic/57846/)** | README; attribution; project brief; refs | Дата, explicit continuity й repository link доступні. Це author-reported history, не independent causal validation. | Залишити history. Exact external article title не переписувати під новий тон report. C30. |
| **S-2025-01 — Deloitte enterprise survey** | R1 Ch3 + refs | Generic URL тепер 2026. Linked previous report — Jan2025/Q4, survey Jul–Sep2024, n2,773; заявлений Q3 2025 не ідентифікований. Є позитивні ROI результати, не лише scaling friction. | Market context, після pin edition; не доказ «AI не delivered». C16. |
| **S-2025-02 — [McKinsey 2025 original](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025)** | R1 Ch3 already original link; REFERENCES помилково secondary-only | 88% adoption / 6% high performers / 39% reporting enterprise EBIT impact — різні definitions. 6% не всі з meaningful ROI. Causal 82-point infrastructure explanation не встановлено. | Market adoption section; register original distinct from third-party summary, amend classification rationale. C15. |
| **S-2025-03 — Artur Markus, Inference Cost Paradox** | R1 Ch2 | Secondary commentary dated Jan2 2026; заголовок повторює arithmetic error. Underlying Menlo market estimate й CloudZero planned spend не software maintenance outcome. | Короткий cost-demand context або appendix; original sources separately registered. C13–C14. |
| **S-2026-01 — Andreas Horn** | R1 Ch3, два posts; refs/README | Personal forecasts/commentary; не IBM endorsement і не незалежна validation METR. Другий post — окремий object. Historical role потребує pin або пропуску. | Market narrative box після даних; не опора механізму. C17. |
| **S-2025-04 — [SoftwareSeni](https://www.softwareseni.com/why-ai-coding-speed-gains-disappear-in-code-reviews/)** | R1 Ch4 refs | Не підтримує заявлені 2–3×. Цитує різні studies/populations, зокрема Faros +91% review time. Не можна їх злити. | Discovery/context у brief; прямі quantitative claims перенести на reviewed originals. C19. |
| **S-2025-05 — TechnoDiaries** | R1 Ch1 fear/burnout refs | Доступний один first-person doubled-review anecdote; решта member-only. Не plural empirical sample чи оцінка senior population. | Practitioner hypothesis/context box; не кількісна triangulation. C20. |
| **M-1984-01 — Goldratt, The Goal** | R1 Ch4; R2/R3 interpretation; README methodology | Useful interpretive framework. Повний edition/page trace не перевірений. Не вимірює AI effect і не доводить один незмінний bottleneck або inevitable harm. | Model section Ch4 із assumptions, alternatives, falsifiers. C21–C22. |

## Конкретні claims, числа і місця виправлення

Severity: **P0** змінює central inference або є явною factual error; **P1** істотно звужує scope/твердження; **P2** навігація/traceability. Усі повтори одного claim треба знаходити repository-wide, а не виправляти лише наведений рядок.

| Claim | Priority / locator у baseline | Потрібна дія й критерій правильності |
| --- | --- | --- |
| **C01** | P0 R1:77,185, Peng | Замінити n196; розділити randomized і completers. «55.8% less completion time» з task/sample, не +55.8% general delivery throughput. |
| **C02** | P1 R1:23–31,182, METR | +19% elapsed time, early2025 setting; не permanent senior penalty. Зіставити з [Feb2026 follow-up](https://metr.org/blog/2026-02-24-uplift-update/): selection problems не дають надійно оцінити сучасний розмір ефекту. Не перетворювати follow-up на нову універсальну speedup claim. |
| **C03** | P0 R1:32–40,183,474, Xu | Виправити sample, core/peripheral definitions, review-count units; не ототожнювати study role зі seniority. |
| **C04** | P0 R1:77–79, Xu | Bottom quartile ≠ all peripheral/juniors; прибрати «aggregate project gain disappears». Відділити authors' estimates, identification assumptions і repository hypothesis про redistribution. |
| **C05** | P0 R1:44–49,174,184,460,476,508 | Прибрати per-feature/per-unit +39%, measured cognitive-load і «functionally correct but convoluted». Розділити code metric, warning count, maintainability hypothesis і production defects. |
| **C06** | P1 R1:53–62,186; R2:94,107 | Розвести GitClear data objects; точні numerator/denominator/time windows для duplication/reuse. Full quality report access залишається open; «10 files» не universal token/context limit. |
| **C07** | P0 R1:63–68 | `(6.1+14.1)/2=10.1`, а авторські `9.0=(6.8+6.1+14.1)/3`. Навіть правильне середнє різних proxies не є validated «net productivity». Краще показати метрики окремо. Reviewer також виявив internal Method1 mean discrepancy (+34.1% у method section / +7.1% у summary): не обирати зручне число без resolution. |
| **C08** | P0 R1:55–60,460,507; R2:27 | +131.1% mean lines із іншого report/sample не доказ doubling кожного team's input. Припинити causal chain, складений із несумісних study percentages. |
| **C09** | P1 R1:85–115; R2:128–172; NBER brief | Зберегти позитивні releases й усі cumulative/model/observational qualifiers. Table5 marginal async release відсутній; supplied PDF prose20.2 vs table20.3 також потребує exact locator, якщо вводиться decimal precision. |
| **C10** | P0 R2:162–170, «most organizations»; README map boundary | NBER не вимірює prevalence bottleneck у більшості організацій. Map уже коректно називає synthesis — не зробити його знов «доведеним ланцюгом». Наочна neutral/success branch допоможе, але потребує окремого synthesis review. |
| **C11** | P0 R1:219–225,299–302 | Виправити R&D і FY/CY; для Meta звірити definition CapEx. 2025 guidance має date/as-of і свій original. Вилучити unsupported ~$64B CY run-rate або показати calculation/period. Corporate totals не AI-coding enabling cost. |
| **C12** | P1 R1:210–217,298; REFERENCES:60 | Book2020; точний TAP scale за Ch23. $1B/$1–3B/10–15years cost assertions не отримують доказовість від посилання на опис практик. Critique не «replaces any need for a human». |
| **C13** | P0 R1:234–258,276–284 | `$19*12*1000=$228,000`; component sums7–27M арифметично правильні, premise не обґрунтовано. Ratios30.7–118.4× conditional; license share0.84–3.26% від transformation-only denominator. Розділити one-off/recurring/incremental/allocated costs. Перенести в явно illustrative sensitivity model або вилучити. |
| **C14** | P0 R1:264–268 | `(37/11.5-1)*100=221.739%`; 3.217× =321.739% **від** baseline. [Menlo original](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) — modelled market sizing із revised baseline. [CloudZero](https://www.cloudzero.com/state-of-ai-costs/)85,521/45% у body — planned spend, не realized all-enterprise spend; Key takeaways водночас каже43%≥100k замість45%>100k. Pin exact question/chart/threshold і зберегти internal discrepancy. 1000× period/capability не підтверджено. Jevons — interpretation, не доведена AI-code-debt причина. |
| **C15** | P0 R1 Ch3 «88% / 6% / 82-point gap», ref397 | Correct definitions; don't infer missing infrastructure caused all gap. Quantitative survey != causal explanation; preserve positive impact. |
| **C16** | P1 R1:383,401; REFERENCES:89 | Pin Deloitte edition or mark unresolved; замінити «implicit acknowledgment ... has not delivered» на observed survey findings із позитивними й негативними частинами. |
| **C17** | P1 R1:348–354,399–402 | Horn opinion не verification. Microsoft FY25Q2 statement стосується total AI business annual revenue run-rate >$13B, не «record Copilot revenue». «Execution mandate» — hypothesis, не source finding. |
| **C18** | P0 R1:398; R2:42–51,77 | Pin originalMarch study separate from updated graph/GPT5.2. 50% horizon != global reliability; horizon trend != exponential liability/volume/complexity. |
| **C19** | P0 R1:535 | Прибрати 2–3×review-time attribution SoftwareSeni. [Faros original](https://www.faros.ai/blog/ai-software-engineering) — окремий commercial observational source, не Xu і не universal estimate. |
| **C20** | P1 R1:119–128,188–189 | Fear→overtime→apparent productivity не встановлено. [Stack Overflow2024](https://survey.stackoverflow.co/2024/ai) не підтверджує наведений fear trend; 70% professionals не сприймали AI як job threat. Anecdote не plural sample. |
| **C21** | P0 R1:414–425,525 | Усунути суперечність «coding was natural bottleneck» / «step didn't need optimization». Queue growth умовне: admitted work rate, service capacity, risk/task size, utilization/variance. |
| **C22** | P0 R1:470–496; R2:54–64 | «Deep review або rubber stamp» — false dichotomy. Додати WIP/pull controls, smaller changes, task selection, automation, training, capacity changes та можливість net improvement. |
| **C23** | P1 R2:23–51,65–73 | 3–5 juniors,10+effective devs,10sec/30min, mentorship collapse — illustrative assumptions/hypotheses без population estimate. Не поєднувати їх із GitClear як виміряний multiplier. |
| **C24** | P0 R2 Ch6; R3:19–31 | «Case study» фактично thought experiment. Не «proves» inevitable new bottleneck: врахувати net review saving, operating cost, error rates і comparison. Cross-ref Ch5→Ch6. |
| **C25** | P0 R1:138–176,280–294; R3 Ch10 | Прибрати universal absence «vendor data does not exist», «placebo analytics», guaranteed bankruptcy, assumptions про motives. Evidence gap формулювати щодо виконаного пошуку, scope й outcomes; рекомендації до disclosures залишити. |
| **C26** | P0 R3 Ch8–9 | Прибрати «will destroy enterprise», «entire system must redesigned», industry already at precipice; low/high probability без model. Додати adaptation/success і null/mixed paths поряд із ризиками. |
| **C27** | P0 R3 Ch10 «Vendors», «Stewards of Capital» | Видалити parasitic/host/extractive accusations і юридичний висновок fiduciary violation. Критикувати measurable commercial incentives, product defaults, claim scope, evidence disclosure. Імена компаній — лише для attributed конкретних перевірених claims. |
| **C28** | P1 R1:79,145; R3 Ch9 та illustrative passages | 80–90%brownfield,80%postdeployment cost,80–90%futuremaintenance,6/18months,30PR queue, exponential conflicts — inventory кожного occurrence; source with matching denominator або explicitly hypothetical/remove. |
| **C29** | P1 attribution + terminology brief | Зберегти historic observations; додати dated current drift/access limitations. «Independent convergence» замінити на separately published works; relationships not established. Відсутність доказу впливу не доводить незалежності. |
| **C30** | P1 project brief:85–96,140 + attribution | Створення repository object ≠ public visibility на цю дату; author-reported name origin ≠ independently documented origin. Не змінювати exact external titles. |
| **C31** | P2 Protocol1 flowchart; R3:19 | Systemic Cure — Protocol4, не3; hypothetical review-agent example — Ch6, не5. Оновити TOC/anchors після заголовків. |
| **C32** | P1 Protocol1 Green/Disposable zones; Protocol2 §2 step3 | Disposable script може irreversibly mutate persistent data; migration не low risk через коротке життя коду. У Protocol2 зростання wait/rework/failure саме по собі не доводить throughput decrease: виміряти releases/throughput або сказати «delivery health deteriorated». |
| **C33** | P1 Protocol4 §§1,5; protocol titles/index | More generated output не обов'язково more admitted downstream work. Capacity responses — conditional control patterns, не empirical universal cure; success оцінює pilot #54. |

## Джерела поза реєстром або з нечіткою ідентичністю

| Object / location | Наступна дія |
| --- | --- |
| Stack Overflow2024, R1:189 | Зареєструвати original survey, exact question/sample/year; прибрати unsupported fear/overtime inference. |
| Faros enterprise report, discovered via SoftwareSeni | Flow E→A лише якщо зберігається в report; commercial conflict, observational association, review time vs count. Його >10k developers/1,255teams — окремий sample, не виправлення Xu «без сліду». |
| METR Feb24 2026 follow-up | Окремий temporal update до RCT; selection/measurement limitations обов'язкові. |
| Anthropic skill formation, existing #4 | Використати існуюче issue; перевірити original study, learning/debugging outcomes і training conditions. Не підбирати лише anti-AI висновки. |
| Menlo2025, CloudZero2025, R1 Ch2 via Markus | Окремі source records для retained numbers; market model / planned spending definitions; potential commercial interests. |
| Copilot price, R1:236; Pichai10%, R1:226 | Price pin as-of/plan/seat assumptions; CEO interview — first-party estimate з методологічним обмеженням, не RCT. Не тихо підміняти історичну ціну поточною. |
| FT via delo, Xenoss, Epoch, R1:302–305 | Для кожного визначити actual claim і original source. Проміжний media/industry link не proof of enterprise transformation TCO. Remove if no retained claim. |
| McKinsey original + third-party summary | Original уже використано в R1, REFERENCES/source row застарілі. Розділити objects або документувати replacement; survey authors' original data не derivative evidence. |
| Deloitte moving URL | Pin exact edition/PDF; don't label latest landing page Q32025. |
| Horn second post; Microsoft FY25Q2, R1:400/402 | Окремі publication objects; personal opinion vs company business record. |
| AgileMindset, R1:534; Goldratt edition | Theory/framework role; edition/pages. Не робити AI-causal conclusion з management analogy. |
| DORA, README:74 | Identify year/report/actual reliance; якщо декоративна незадіяна назва — прибрати з evidence map, не створювати уявну empirical support. |
| `uncertainty-architecture` spec, protocols index/04 | Позначити methodological relationship із власним проєктом, не independent validation і не organizational endorsement. |

## Рекомендована архітектура тексту

Зберегти проектну назву можна як назву дослідницької гіпотези. Не потрібно косметично «обезбарвлювати» все. Потрібно, щоб headings, charts, summaries і висновки мали ту саму силу, що й evidence. Локальне слово *may* не виправляє категоричний заголовок чи звинувачувальну метафору.

| Розділ | Що залишити / змінити | Краще місце доказів |
| --- | --- | --- |
| Ch1 | «What the evidence measures: heterogeneous effects and delivery attenuation». Study comparison: design, sample, tool/date, outcome, positive/null/negative, limits. | METR/Peng/Xu/Agarwal/GitClear окремими рядками; NBER завершує synthesis. |
| Ch2 | «Costs beyond licenses: a conditional TCO model». Невідомі cost estimates явно assumptions. | Engineering practice приклади в тексті; corporate filing totals і sensitivity table в appendix або вилучити. |
| Ch3 | «Adoption incentives and the evidence gap». Не market psychology як установлений факт. | McKinsey/Deloitte contextual survey; Horn/company statements окремий narrative box. |
| Ch4 | «A conditional model of downstream constraints». Assumptions→mechanism→alternatives→falsifiers. | Goldratt як methodology; empirical results cross-referenced, без mixed-study numeric chain. |
| Ch5 | «Review capacity and verification risk». Queue, active effort, defects, mentor time — різні outcomes. | METR task-horizon measurement box; anecdote відділити від study evidence. |
| Ch6 | «A thought experiment: operating an AI review system». Compare total workload and error outcomes. | Measured case study only if actual organization/data/protocol exists; інакше thought experiment. |
| Ch7 | «From code to release: where gains attenuate». Усунути повтор повної NBER таблиці. | Короткий NBER link; human-capacity mechanism лишається calibrated interpretation. |
| Ch8 | «When local improvements improve the whole system». Proportional intervention, success conditions. | Не нове empirical твердження без source; зіставити із protocols2/4. |
| Ch9 | «Conditional scenarios and observable signals». Risk, adaptation, mixed/null; no calibrated probability labels without model. | Leading/lagging indicators і falsification matrix з #54. |
| Ch10 | «Responsibilities for measurement and adoption». Accountability, claim disclosures, product/organizational controls. | Перевірені examples із точним speaker/date; без vendor motives, biology metaphors та legal verdicts. |

Приклади заміни:

- «The vendor data does not exist» → “The sources reviewed here do not establish a general reduction in enterprise maintenance cost or defect rates. This is a limitation of this evidence set, not proof that no relevant evidence exists.”
- «AI code review only shifts the burden» → “Automated review may reduce manual work while creating operating and oversight costs. Its net effect should be measured against the previous review process.”
- «The parasitic model kills the host» → “Commercial incentives may favor adoption or usage metrics that do not fully represent customers' long-term delivery outcomes. This potential misalignment should be assessed through published outcome measures.”
- «The system must be redesigned as a whole» → “Teams should identify the constraints that actually changed and test proportionate adjustments before expanding adoption.”

## Що може спростувати або звузити механізм

| Hypothesis | Що вимірювати | Результат, який послаблює тезу |
| --- | --- | --- |
| H1: generation increases admitted work faster than downstream capacity | AI exposure, change/risk size, admitted WIP, wait vs active review time, throughput | Coding time падає; WIP, quality і review effort стабільні; більше successful releases |
| H2: review burden displaces other senior work | Role/activity definitions, sampled review hours, implementation/mentoring time, team outcomes | Automation зменшує total review effort; mentor time/outcomes не погіршуються |
| H3: code-structure proxies predict higher maintenance cost | Matched cohorts, LOC-normalized metrics, defects, maintenance hours, follow-up | Complexity/churn зростають без гірших defects/costs або користь перевищує витрати |
| H4: incentives privilege activity over outcome | Actual contracts/defaults/disclosures and decisions | Vendors/customers use outcome measures; incentives align with quality/value |
| H5: local constraints accumulate into macro crisis | Predefined population, transmission mechanism, longitudinal indicators | Adaptation absorbs load; risk remains local; net outcome improves |

Це план перевірки, не нова модель з оціненими коефіцієнтами. Для #54 важливі comparable task mix, cost allocation, quality follow-up та self-selection; простий before/after dashboard не автоматично дає causality.

## Черга робіт і розподіл відповідальності

Спочатку review/merge governance PR #56; потім source corrections; після них synthesis/tone; наприкінці repository-wide synchronization. Не починати publishing/release migration поверх тексту з відомими numeric/inference помилками.

Детальні child issues створено після незалежної перевірки цього документа. Кожне має scope/source IDs/claim IDs, instructions, п'ять stable acceptance criteria, prerequisites, review/check/handoff requirements. Existing #4 (skill formation), #54 (measurement pilot), #55 (release/citation), #48–51 (старі publishing/validation PR) зберігають свої scopes.

| Issue | Зміст | Послідовність / роль |
| --- | --- | --- |
| [#57](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/57) | Peng, METR2025, follow-up2026 | Sol: source briefs і точні corrections; analytical review: external validity |
| [#58](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/58) | Xu/Agarwal population, units, inference | Sol: source trace і replacements; analytical review: role/proxy/causality |
| [#59](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/59) | Два GitClear reports і composite metrics | Sol: access/definitions/tables; analytical review: interpretation і source-internal contradictions |
| [#60](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/60) | Filings, infrastructure claims, conditional TCO | Sol: originals/calculation; author/analytical reviewer: retain/remove model, cost allocation |
| [#61](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/61) | Surveys, market narrative, secondary/orphan sources | Sol: source identity/trace; analytical review: selective framing/inference |
| [#62](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/62) | Terminology/project provenance | Sol: dated observations; separate documentary reviewer: disputed/limited chronology |
| [#63](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/63) | NBER і спростовуваний delivery mechanism | Після #57–59; analytical agent веде model/alternatives, Sol інтегрує approved wording; зв'язок із #54 |
| [#64](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/64) | Neutral conclusions/scenarios, Chapters1–10 | Після source corrections і #63; author/analytical decision, Sol systematic edits |
| [#65](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/issues/65) | Protocols, navigation, complete occurrence closure | Після #57–64; Sol synchronization/checks; separate final research review |

Перші шість issue можуть виконуватися незалежними bounded PR за умови узгодження overlapping edits у R1. Їхня незалежність не дозволяє паралельно переписувати один абзац без координації. Не потрібно чекати на всі source tasks, щоб підготувати аналітичний draft #63, але його фінальні висновки мають спиратися на перевірений evidence.

**Sol:** відкрити pinned originals; створити briefs за шаблоном; exact numbers/units/versions; exhaustive occurrence search; виконати узгоджені bounded replacements; bibliography/current-use/index synchronization; arithmetic і navigation checks; PR із AC evidence. Це добре обмежувана робота. Sol має повідомляти про суперечність original із завданням, а не слухняно переносити помилку аудиту.

**Аналітичний агент / автор:** strength of causal inference; чи можна переносити ефект між populations; як зберегти positive/null results у центральній тезі; вибір місця джерела; conditional mechanism і alternatives/falsifiers; neutral framing і attribution disputes; final independent review. Ці рішення не варто ховати в mechanical copy-edit завданні.

Один agent може реалізувати source brief і синхронізацію, але незалежне підтвердження має виконати інший reviewer, як вимагає AGENTS. Tests не доводять research accuracy. `Verified` можливе лише після повного Flow, `Confirmed` і інтеграції required corrections у default branch; open blockers не закривати checkbox-ом.

## Незалежна перевірка і статус

- Перший незалежний evidence reviewer: `/root/independent_evidence_review`, 2026-10-20. Самостійно перевірив secondary/documentary/provenance surfaces, omitted citations і Xu original. Outcome щодо поточної research integration: **Corrections required**. Зокрема підтвердив Xu sample/unit issues, SoftwareSeni mismatch, StackOverflow/Deloitte scope, provenance drift і GitHub creation/visibility distinction.
- Governance/RI reviewer: `/root/independent_governance_review`, 2026-10-20. Outcome **Confirmed** для implementation scope; 118 tests, validator, evidence-state check, RI verify пройшли. Не є підтвердженням цього evidence audit чи final committed CI.
- Фінальний незалежний reviewer цього artifact: `/root/independent_evidence_review`, 2026-10-20. Outcome: **Confirmed для audit/remediation plan**, після виправлення visibility overclaim і додавання GitClear/CloudZero internal discrepancies. Перевірено 25/25 source coverage, ключові primary corrections і supplied NBER PDF. Review не охоплює remote issue bodies як окремі implementations і не підтверджує поточну research integration.
- Source states лишаються незмінними; усі research findings вище — open remediation до окремих implementation PR. Outcome щодо поточної research integration: **Corrections required**; не `Verified`.
