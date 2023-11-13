class CMDBase {
    /**
     * @param {{base_url: string, autocomplete_pause: number, debug: boolean}} options 
     */
    constructor({base_url, autocomplete_pause, debug}) {
        this.base_url = base_url
        this.autocomplete_pause = autocomplete_pause
        this.debug = debug

        // cache
        this._today_date = null
        this._today_month = null
        this._today_year = null
    }

    is_today(date) {
        if (! date) {
            return false
        }

        if (! this._today_date) {
            let today = new Date()
            this._today_date = today.getDate()
            this._today_month = today.getMonth()
            this._today_date = today.getFullYear()
        }
        
        return date.getDate() == this._today_date && date.getMonth() == this._today_month && date.getFullYear() == this._today_date
    }
}

/**
 * @type {CMDBase}
 */
let cmdbase = null

function get_cmdbase() {
    if (cmdbase === null) {
        throw new Error(`cmdbase not configured`)
    }
    return cmdbase
}

// Default bootstrap table

function server_bootstrap_table(selector, options) {
    $(selector).bootstrapTable({
        pagination: true,
        pageSize: 100,
        sidePagination: 'server',
        dataField: 'results',
        totalField: 'count',
        queryParams: function({limit, offset, search, sort, order}) { return {limit, offset, search, ordering: order == 'desc' ? `-${sort}` : sort}},
        ...options
    })
}

// Formatters for bootstrap table

function datetime_formatter(value) {
        if (! value)
            return ""
        const date = new Date(value)
        const str = date.toLocaleString()
        const pos = str.indexOf(' ')
        if (pos <= 0) {
            return str
        }
    
        if (cmdbase.is_today(date)) {
            return `<span title="${str}">${str.substring(pos + 1)}</span>`
        }
        else {
            return `<span title="${str}">${str.substring(0, pos)}</span>`
        }
}


function field_formatter(display_field, {url_field, url_template} = {}) {
    function formatter(value, row) {
        let result = `<span title="${value}">${row[display_field]}</span>`
        if (url_field) {
            result = `<a href="${row[url_field]}">${result}</a>`
        }
        else if (url_template) {
            const url = url_template
                .replace('${base_url}', cmdbase.base_url)
                .replace('${value}', value)
            
            result = `<a href="${url}">${result}</a>`
        }
        return result
    }

    return formatter
}


function choices_formatter(field_name) {
    const pairs = Choices.pairs(field_name) // Produced by Python module `django_js_choices`

    function formatter(value) {
        for (let pair of pairs) {
            if (pair.value == value) {
                return `<span title="${value}">${pair.label}</span>`
            }
        }
        return value
    }

    return formatter
}
