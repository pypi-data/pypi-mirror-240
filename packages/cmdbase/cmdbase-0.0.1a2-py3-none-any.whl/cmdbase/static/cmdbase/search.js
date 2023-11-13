/// <reference path="base.js" />

/**
 * @param {string} form_id 
 */
function bind_cmdbase_search_form(form_id) {
    function display_item_or_category(result) {
        let html = ""

        if (result.category_name) {
            html += `<a href="${cmdbase.base_url}/-/${result.category_slug}/${result.slug}">${result.name}</a> (<a href="${cmdbase.base_url}/-/${result.category_slug}">${result.category_name}</a>)`
            if (result.source && result.value) {
                html += `&nbsp;&nbsp;&nbsp;<small class="text-secondary">[${result.source}: ${result.value}]</small>`
            }
        }

        else {
            html += `<a href="${cmdbase.base_url}/-/${result.slug}">${result.name}</a> <i>(Category)</i>`
        }

        return html
    }

    async function fetch_search(search) {
        if (!search) {
            return ""
        }
    
        const limit = 20
        const url = cmdbase.base_url + `/api/search?` + new URLSearchParams({search, limit: limit+1})
        let t0;
        if (cmdbase.debug) {
            console.log(`search fetch`, url)
            t0 = performance.now()
        }

        const response = await fetch(url)
        if (! response.ok) {
            throw new Error(`${response.status} ${response.statusText}`)
        }
        if (cmdbase.debug) {
            console.log(`search response: ${Math.round(performance.now() - t0)} ms`, response.status, response.statusText)
        }

        const results = await response.json()
        if (results.length == 0) {
            return ""
        }
        
        let html = `<ul>`
        for (let i = 0; i < results.length; i++) {
            if (i == limit) {
                html += `\n<li>... <i><a href="${cmdbase.base_url}/?search=${encodeURIComponent(search)}&limit=${encodeURIComponent(limit * 2)}"><i class="bi bi-plus-circle-dotted"></i> More</a></i> ...</li>`
                break;
            }

            html += `<li>${display_item_or_category(results[i])}</li>`
        }
        html += `</ul>`
        return html
    }

    const form_elem = document.getElementById(form_id)
    const input_elem = form_elem.querySelector("input")
    const button_elem = form_elem.querySelector("button")
    const result_elem = form_elem.querySelector(".autocomplete-result")

    const original_button_innerHTML = button_elem.innerHTML

    function start_loading() {
        button_elem.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span class="visually-hidden">Loading...</span>`
        button_elem.disabled = true
    }

    function stop_loading() {
        button_elem.disabled = false
        button_elem.innerHTML = original_button_innerHTML
    }

    class SearchQueue {
        constructor() {
            this._is_consuming = false
            this._input = null // only the last input will be searched
        }

        async append(input) {
            this._input = input

            if (! this._is_consuming) {
                this._consume()
            }
        }

        async _consume() {
            this._is_consuming = true
            start_loading()

            // wait some time for additional keys to be pressed
            await new Promise(r => setTimeout(r, cmdbase.autocomplete_pause * 1000));

            const input = this._input
            this._input = null
            
            try {
                result_elem.innerHTML = await fetch_search(input)
            }
            catch (err) {
                result_elem.innerHTML = `<div class="text-danger">${err}</div>`
            }

            result_elem.style.visibility = result_elem.innerHTML ? "visible" : "hidden"

            if (this._input) {
                await this._consume()
            }

            stop_loading()
            this._is_consuming = false
        }
    }

    const queue = new SearchQueue()

    form_elem.addEventListener("input", async function(ev) {
        let input = input_elem.value.trim()
        queue.append(input)
    })
  
    // Hide resultElem if click outside of resultElem and inputElem
    document.addEventListener("mouseup", function(ev) {
        // If the target of the click isn't resultElem
        if (ev.target != result_elem && !result_elem.contains(ev.target) && ev.target != input_elem && !input_elem.contains(ev.target)) {
            result_elem.style.visibility = "hidden"
        }
    })
    
    // Show again resultElem if come back over formElem
    form_elem.addEventListener("mouseover", function(ev) {
        result_elem.style.visibility = result_elem.innerHTML ? "visible" : "hidden"
    })
}
