import { QuartzConfig } from './quartz/cfg'
import * as Plugin from './quartz/plugins'

// Only a selected staging directory is rendered. UA content, graph emitters,
// analytics and publication-specific transformations are intentionally absent.
const colors = {
  light: '#ffffff', lightgray: '#e5e5e5', gray: '#888888', darkgray: '#444444',
  dark: '#111111', secondary: '#284b63', tertiary: '#526b76',
  highlight: '#eeeeee', textHighlight: '#fff3b0',
}
const config: QuartzConfig = {
  configuration: {
    pageTitle: 'The Subprime Code Crisis', pageTitleSuffix: '',
    enableSPA: false, enablePopovers: false, analytics: null,
    locale: 'en-US', ignorePatterns: [], defaultDateType: 'published',
    theme: {
      fontOrigin: 'local', cdnCaching: false,
      typography: { header: 'Arial', body: 'Arial', code: 'monospace' },
      colors: { lightMode: colors, darkMode: colors },
    },
  },
  plugins: {
    transformers: [Plugin.FrontMatter(), Plugin.GitHubFlavoredMarkdown(),
      Plugin.CrawlLinks({ markdownLinkResolution: 'relative' }), Plugin.Description()],
    filters: [], // publish.py owns explicit draft/public selection before staging.
    emitters: [Plugin.ComponentResources(), Plugin.ContentPage(), Plugin.Assets(), Plugin.Static()],
  },
}
export default config
