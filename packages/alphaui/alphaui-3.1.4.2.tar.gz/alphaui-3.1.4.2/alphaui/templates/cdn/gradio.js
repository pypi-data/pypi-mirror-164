

function make_script(src) {
    const script = document.createElement('script');
    script.type = 'module';
    script.setAttribute("crossorigin", "");
    script.src = src;
    document.head.appendChild(script);
}
make_script("https://gradio.s3-us-west-2.amazonaws.com/3.1.4/assets/index.342fe35e.js");
