
module DashQrcode
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/qrcode.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_qrcode",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "async-QRCode.js",
    external_url = "https://unpkg.com/dash_qrcode@0.0.1/dash_qrcode/async-QRCode.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-QRCode.js.map",
    external_url = "https://unpkg.com/dash_qrcode@0.0.1/dash_qrcode/async-QRCode.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_qrcode.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_qrcode.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
