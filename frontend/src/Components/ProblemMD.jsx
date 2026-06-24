import { useEffect, useState } from 'react';
import { Marked } from 'marked';
import { markedHighlight } from 'marked-highlight';
import hljs from 'highlight.js';
import 'highlight.js/styles/atom-one-dark.css';

const marked = new Marked(
  // extension handle code block highlights
  markedHighlight({
    emptyLangClass: 'hljs',
    langPrefix: 'hljs language-',
    highlight(code, lang) {
      const language = hljs.getLanguage(lang) ? lang : 'plaintext';
      return hljs.highlight(code, { language }).value;
    }
  })
)

const renderer = {
  paragraph(text) {
    // render link as usual
    if (text.tokens.some(t => t.type === 'link')) {
        console.log(text)
      return `<p>${this.parser.parseInline(text.tokens)}</p>`
    }
    // render paragraph preserving space and tabs
    return `<p class="pre-like">${text.text}</p>\n`;
  }
};

marked.use({ renderer });

function ProblemMD({ mdfile }) {
  const [htmlContent, setHtmlContent] = useState('Loading...');


  useEffect(() => {
    // Fetch the file from the public directory
    async function fetchMD() {
      try {
        const response = await fetch(`/problems/${mdfile}`);
        if (!response.ok) {
          throw new Error(mdfile + " file fetch error");
        }
        const content = await response.text()
        setHtmlContent(marked.parse(content))
      } catch (err) {
        console.error("Error loading markdown:", err)
      };
    }
    fetchMD();
  }, [mdfile]);

  return (
    <div
      dangerouslySetInnerHTML={{ __html: htmlContent }}
    />
  );
}

export default ProblemMD;