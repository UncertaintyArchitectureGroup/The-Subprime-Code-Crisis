import { PageLayout, SharedLayout } from './quartz/cfg'
import * as Component from './quartz/components'

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(), header: [], afterBody: [],
  footer: Component.Footer({ links: {
    Repository: 'https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis',
  } }),
}
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [], left: [], right: [],
}
export const defaultListPageLayout: PageLayout = defaultContentPageLayout
