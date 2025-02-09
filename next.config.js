/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  basePath: '/arxiv_summary_viewer',
  assetPrefix: '/arxiv_summary_viewer/',
}

module.exports = nextConfig