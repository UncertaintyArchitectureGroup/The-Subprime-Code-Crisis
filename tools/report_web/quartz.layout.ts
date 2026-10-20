import { PageLayout, SharedLayout } from "./quartz/cfg"
import { ReportHead, ReportHeader, ReportContents, ReportMeta, ReportFooter } from "./report-components"

export const sharedPageComponents: SharedLayout = {
  head: ReportHead, header: [ReportHeader], afterBody: [], footer: ReportFooter,
}
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [ReportMeta], left: [ReportContents], right: [],
}
export const defaultListPageLayout = defaultContentPageLayout
