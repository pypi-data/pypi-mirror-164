# AUTO GENERATED FILE - DO NOT EDIT

#' @export
qRCode <- function(id=NULL, result=NULL, scanDelay=NULL, status=NULL) {
    
    props <- list(id=id, result=result, scanDelay=scanDelay, status=status)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'QRCode',
        namespace = 'dash_qrcode',
        propNames = c('id', 'result', 'scanDelay', 'status'),
        package = 'dashQrcode'
        )

    structure(component, class = c('dash_component', 'list'))
}
