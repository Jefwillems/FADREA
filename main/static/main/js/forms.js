const forms = (function () {
    let app = Object.create(null);
    let helpFields = [];
    let inputs = [];

    let appendHelpers = function () {
        let fields_input = Array.prototype.slice.call(document.querySelectorAll("input"));
        fields_input = fields_input.map(input => {
            if (input.name !== 'csrfmiddlewaretoken') {
                let hint = document.createElement('div');
                hint.setAttribute("class", "hint");
                let icon = document.createElement("i");
                icon.setAttribute("class", "material-icons");
                icon.innerText = "help_outline";
                hint.appendChild(icon);
                let container = document.createElement('div');
                container.setAttribute("class", "form-input");
                input.parentElement.insertBefore(container, input.nextSibling);
                container.appendChild(input);
                container.appendChild(hint);
                let helptext = container.parentNode.lastChild;
                if (container.parentNode.nextSibling.localName === 'ul') {
                    helptext.appendChild(container.parentNode.nextSibling);
                }
                if (helptext !== null && helptext.className === 'helptext') {
                    return {input, hint, helptext};
                }

                return {input, hint};
            }
            return null
        });
        return fields_input.filter(e => e !== null);
    };
    let cacheDom = function () {
        helpFields = [];
        let field_ul = document.querySelectorAll("form ul");
        field_ul.forEach(e => {
            helpFields.push(e);
        });
        let field_p = document.querySelectorAll("form .helptext");
        field_p.forEach(e => {
            helpFields.push(e);
        });

        inputs = appendHelpers();
    };

    let addListeners = function () {
        inputs.forEach(e => {
            e.hint.onmouseover = (event) => {
                if (e.helptext) {
                    e.helptext.setAttribute('style', 'display: block');
                }
            };
            e.hint.onmouseleave = (event) => {
                if (e.helptext) {
                    e.helptext.setAttribute('style', '');
                }
            }
        })
    };

    app.init = function () {
        cacheDom();
        addListeners();
    };
    return app;
})();

forms.init();