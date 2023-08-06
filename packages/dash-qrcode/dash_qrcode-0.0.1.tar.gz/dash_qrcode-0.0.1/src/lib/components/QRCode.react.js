import PropTypes from 'prop-types';
import React, { Component, lazy, Suspense } from 'react';
import { QrReader } from 'react-qr-reader';

/**
 * A Dash component for reading QR codes from an attached webcam.
 */
export default class QRCode extends Component {

    constructor(props) {
        super(props);

        this.handleClickScan = this.handleClickScan.bind(this);
        this.handleScan = this.handleScan.bind(this);
        this.handleError = this.handleError.bind(this);
    }


    handleClickScan = () => {
        const { setProps, status } = this.props;
        setProps({
            result: null,
            status: status === 'reader' ? 'idle' : 'reader',
        });

    };

    handleScan = data => {
        const { setProps } = this.props;
        if (data) {
            setProps({
                result: data.text,
            });
        }
    };

    handleError = err => {
        console.error(err);
    };

    render() {
        const {
            scanDelay, status
        } = this.props;
        const { id, loading_state } = this.props;
        if (status === 'reader') {
            return (
                <div
                    id={id}
                    data-dash-is-loading={
                        (loading_state && loading_state.is_loading) || undefined
                    }>
                    <QrReader
                        scanDelay={scanDelay}
                        onError={this.handleError}
                        onResult={this.handleScan}
                        style={{ width: '100%' }}
                    />
                </div>
            );
        }
        return (
            <div
                id={id}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
            >

            </div>
        );
    }
}


QRCode.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,

    /**
     * Delay for the scanning in ms.
     */
    scanDelay: PropTypes.number,

    /**
     * Prop that will contain the result
     */
    result: PropTypes.string,

    /**
     * Contains the status of the renderer
     */
    status: PropTypes.string,
};

QRCode.defaultProps = {
    scanDelay: 2000,
    result: null,
    status: 'idle',
};