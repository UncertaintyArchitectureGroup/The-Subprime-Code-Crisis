// Quartz's ContentPage deliberately skips directory indexes. Emit only the
// explicitly staged indexes, without FolderPage's inferred/synthetic pages.
import { Content } from "./quartz/components"
import { renderPage, pageResources } from "./quartz/components/renderPage"
import { QuartzEmitterPlugin } from "./quartz/plugins/types"
import { write } from "./quartz/plugins/emitters/helpers"
import { pathToRoot } from "./quartz/util/path"
import { sharedPageComponents, defaultContentPageLayout } from "./quartz.layout"

export const ReportIndexes: QuartzEmitterPlugin = () => ({
  name: "ExplicitReportIndexes",
  async *emit(ctx, content, resources) {
    const allFiles = content.map(([, file]) => file.data)
    const layout = { ...sharedPageComponents, ...defaultContentPageLayout, pageBody: Content() }
    for (const [tree, file] of content) {
      const slug = file.data.slug!
      if (!slug.endsWith("/index")) continue
      const externalResources = pageResources(pathToRoot(slug), resources)
      const props = { ctx, fileData: file.data, cfg: ctx.cfg.configuration, tree, allFiles, children: [], externalResources }
      yield await write({ ctx, slug, ext: ".html", content: renderPage(ctx.cfg.configuration, slug, props, layout, externalResources) })
    }
  },
})
