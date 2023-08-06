/*
**  Copyright (C) Optumi Inc - All rights reserved.
**
**  You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
**  To receive a copy of the licensing terms please write to contact@optumi.com or visit us at http://www.optumi.com.
**/

import * as React from 'react'
import { DIV, Global } from '../../Global'

import { UnControlled as CodeMirror } from 'react-codemirror2'

// This code did not work to enable supporting all languages, though they don't recommend enabling all of them
// import glob from 'glob'
// import path from 'path'
// glob.sync('codemirror/mode/**/*').forEach((file: string) => require(path.resolve(file)))

require('codemirror/mode/julia/julia')
require('codemirror/mode/python/python')
require('codemirror/mode/r/r')

interface IProps {
    mode: string
    source: string
    renderInColor: boolean
}

interface IState {}

export default class Script extends React.Component<IProps, IState> {

    public render = (): JSX.Element => {
		if (Global.shouldLogOnRender) console.log('ComponentRender (' + new Date().getSeconds() + ')');
        return this.props.renderInColor ? (
            <DIV className='p-Widget lm-Widget jp-Editor jp-CodeMirrorEditor jp-InputArea-editor'>
                <CodeMirror
                    value={this.props.source}
                    options={{
                        readOnly: 'nocursor',
                        screenReaderLabel: 'jp-mod-readOnly',
                        theme: 'jupyter',
                        mode: this.props.mode,
                    }}
                />
            </DIV>
        ) : (
            <DIV sx={{
                whiteSpace: 'pre-wrap',
                fontFamily: 'var(--jp-code-font-family)',
            }} className='p-Widget lm-Widget jp-Editor jp-CodeMirrorEditor jp-InputArea-editor'>
                {this.props.source}
            </DIV>
        )
    }

    public shouldComponentUpdate = (nextProps: IProps, nextState: IState): boolean => {
        try {
            if (JSON.stringify(this.props) != JSON.stringify(nextProps)) return true;
            if (JSON.stringify(this.state) != JSON.stringify(nextState)) return true;
            if (Global.shouldLogOnRender) console.log('SuppressedRender (' + new Date().getSeconds() + ')');
            return false;
        } catch (error) {
            return true;
        }
    }
}