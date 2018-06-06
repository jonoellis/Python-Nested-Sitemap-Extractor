import urllib2 as ur
import re
import sys
import pandas as pd
argument_sitemap = sys.argv[1]
base_sitemap = ur.urlopen(argument_sitemap)
base_sitemap_lines = base_sitemap.readlines()
output = []
for base_sitemap_step in base_sitemap_lines:
  data = re.findall('<loc>(https:\/\/.+)<\/loc>',base_sitemap_step)
  for sub_sitemap_from_base_sitemap in data:
    sub_sitemap = ur.urlopen(sub_sitemap_from_base_sitemap)
    sub_sitemap_lines = sub_sitemap.readlines()
    for sub_sitemap_step in sub_sitemap_lines:
      data2 = re.findall('<loc>(https:\/\/.+)<\/loc>',sub_sitemap_step)
      for page_from_sub_sitemap in data2:
        row = [page_from_sub_sitemap]
        output.append(row)
df = pd.DataFrame(output)
df.to_csv('sitemap_extract.csv', index=False, header=['SitemapURLs'])
