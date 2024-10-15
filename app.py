from flask import Flask, render_template
import markdown

app = Flask(__name__)

# 마크다운 콘텐츠를 HTML로 변환하는 함수
def render_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return markdown.markdown(content)

@app.route('/')
def index():
    
    content = render_markdown('example.md')
    # index.html 템플릿에 변환된 마크다운 전달
    return render_template('index.html',content=content)

@app.route('/markdown')
def markdown_page():
    # 마크다운 파일을 HTML로 변환
    content = render_markdown('example.md')
    return render_template('markdown.html', content=content)


if __name__ == '__main__':
    app.run(debug=True)
