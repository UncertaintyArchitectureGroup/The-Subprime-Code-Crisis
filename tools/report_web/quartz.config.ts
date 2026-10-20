import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"
import { ReportIndexes } from "./report-indexes"

// The adapter selects inputs first. No upstream research, analytics, graph,
// folder synthesis, publication-specific figures or PDF machinery is enabled.
const config: QuartzConfig = {
  configuration: {
    pageTitle: "The Subprime Code Crisis",
    pageTitleSuffix: " · Subprime",
    baseUrl: "vitaliioborskyi.ai/subprime",
    enableSPA: false,
    enablePopovers: false,
    analytics: null,
    locale: "en-US",
    ignorePatterns: [],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "local", cdnCaching: false,
      typography: { header: "system-ui", body: "system-ui", code: "monospace" },
      colors: {
        lightMode: {
          light: "#f3f1ea", lightgray: "#ccd0c9", gray: "#6c807f",
          darkgray: "#435962", dark: "#172b36", secondary: "#245866",
          tertiary: "#70512d", highlight: "#e8eeea", textHighlight: "#eae1ce",
        },
        darkMode: {
          light: "#111c22", lightgray: "#33464c", gray: "#738f94",
          darkgray: "#afc0c5", dark: "#e6e8e5", secondary: "#78abb0",
          tertiary: "#c2a373", highlight: "#192a31", textHighlight: "#24454f",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.GitHubFlavoredMarkdown({ enableSmartyPants: false }),
      Plugin.ObsidianFlavoredMarkdown({
        comments: false, highlight: false, wikilinks: false, callouts: false,
        mermaid: true, parseTags: false, parseArrows: false,
        parseBlockReferences: false, enableInHtmlEmbed: false,
        enableYouTubeEmbed: false, enableVideoEmbed: false, enableCheckbox: false,
      }),
      Plugin.SyntaxHighlighting(),
      Plugin.TableOfContents({ maxDepth: 3 }),
      Plugin.Description(),
    ],
    filters: [],
    emitters: [
      Plugin.ComponentResources(), Plugin.ContentPage(), ReportIndexes(),
      Plugin.ContentIndex({ enableSiteMap: false, enableRSS: false }), Plugin.Assets(),
    ],
  },
}
export default config
