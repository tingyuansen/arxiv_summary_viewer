import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

function extractFromMarkdown(content: string, section: string): string {
  const regex = new RegExp(`# ${section}\\s+([^#]+)`, 'i')
  const match = content.match(regex)
  return match ? match[1].trim() : ''
}

export default function Home() {
  const papersDirectory = path.join(process.cwd(), 'papers')
  const papers = fs.readdirSync(papersDirectory)
    .filter(filename => filename.endsWith('.md'))
    .map(filename => {
      const filePath = path.join(papersDirectory, filename)
      const fileContent = fs.readFileSync(filePath, 'utf-8')
      
      // Extract title and author from markdown content
      const title = extractFromMarkdown(fileContent, 'Title')
      const authors = extractFromMarkdown(fileContent, 'Author')
      
      return {
        id: filename.replace('_summary_reorganized.md', ''),
        title: title || 'Untitled',
        authors: authors || 'Unknown Authors',
        date: new Date().toISOString().split('T')[0] // fallback date
      }
    })

  return (
    <div>
      <h2 className="text-3xl font-bold mb-8">Recent Papers</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {papers.map((paper) => (
          <div key={paper.id} className="p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow">
            <h3 className="text-xl font-semibold mb-2">{paper.title}</h3>
            <p className="text-gray-600 mb-4">{paper.authors}</p>
            <p className="text-gray-500 text-sm">arXiv: {paper.id}</p>
          </div>
        ))}
      </div>
    </div>
  )
}