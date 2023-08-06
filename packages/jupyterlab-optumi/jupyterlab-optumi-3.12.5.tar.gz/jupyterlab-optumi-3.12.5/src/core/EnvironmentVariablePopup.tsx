/*
**  Copyright (C) Optumi Inc - All rights reserved.
**
**  You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
**  To receive a copy of the licensing terms please write to contact@optumi.com or visit us at http://www.optumi.com.
**/

import * as React from 'react'
import { DIV, Global } from '../Global';

import { Button, CircularProgress, Dialog, DialogContent, DialogTitle } from '@mui/material';
import { CSSProperties, withStyles } from '@mui/styles';
import { ArrowBackIos } from '@mui/icons-material';

import { ServerConnection } from '@jupyterlab/services';
import { NotebookPanel } from '@jupyterlab/notebook';

import { ShadowedDivider } from './ShadowedDivider';
import { TextBox } from './TextBox';
import { EnvironmentVariableIdentity } from '../components/deploy/EnvironmentVariableIdentity'
import { OptumiMetadataTracker } from '../models/OptumiMetadataTracker';
import ExtraInfo from '../utils/ExtraInfo';
import { Colors } from '../Colors';
import { IntegrationType } from '../components/deploy/IntegrationBrowser/IntegrationBrowser';
import { EnvironmentVariableConfig } from '../models/IntegrationConfig';

const StyledDialog = withStyles({
    paper: {
        width: 'calc(min(80%, 600px + 150px + 2px))',
        // width: '100%',
        height: '80%',
        overflowY: 'visible',
        maxWidth: 'inherit',
    },
})(Dialog);

const StyledButton = withStyles({
    startIcon: {
        marginRight: '0px',
    },
    iconSizeMedium: {
        '& > *:first-child': {
            fontSize: '12px',
        },
    }
})(Button);

class EnvironmentVariable {
    key: string
    value: string

    constructor() {
        this.key = '';
        this.value = '';
    }
}

interface IProps {
    // This close action will allow us to get a new set of environment variables when a new one is created
    onClose?: () => any
    sx?: CSSProperties
}

interface IState {
    waiting: boolean
    open: boolean
    addSpinning: boolean
    createSpinning: boolean
    name: string
    errorMessage: string
    variables: EnvironmentVariable[]
}

const defaultState = {
    waiting: false,
    open: false,
    addSpinning: false,
    createSpinning: false,
    name: '',
    errorMessage: '',
    variables: [] as EnvironmentVariable[],
}

export class EnvironmentVariablePopup extends React.Component<IProps, IState> {
    _isMounted = false;

    static LABEL_WIDTH = '144px'

    constructor(props: IProps) {
        super(props);
        this.state = defaultState;
    }

    private handleClickOpen = () => {
        this.safeSetState({ open: true, variables: [new EnvironmentVariable()] });
    }

    private handleClose = () => {
        if (!this.state.waiting) {
            if (this.props.onClose) this.props.onClose();
            this.safeSetState(defaultState);
        }
    }

    private nameHasError = (name: string): boolean => {
        const tracker: OptumiMetadataTracker = Global.metadata;
        const optumi = tracker.getMetadata();
        const integrations = optumi.config.integrations;
        for (var i = 0; i < integrations.length; i++) {
            if (integrations[i].name === name) return true;
        }
        return false;
    }

    private handleCreate = (add?: boolean) => {
        this.safeSetState({ errorMessage: '', waiting: true, addSpinning: false, createSpinning: false })
        if (add) {
            setTimeout(() => {
                if (this.state.waiting) this.safeSetState({ addSpinning: true });
            }, 1000)
        } else {
            setTimeout(() => {
                if (this.state.waiting) this.safeSetState({ createSpinning: true });
            }, 1000)
        }

        const map: any = {}
        for (let variable of this.state.variables) {
            if (variable.key != '' && variable.value != '') {
                map[variable.key] = variable.value;
            }
        }

        const settings = ServerConnection.makeSettings();
        const url = settings.baseUrl + 'optumi/add-integration';
        const init: RequestInit = {
            method: 'POST',
            body: JSON.stringify({
                name: this.state.name,
                info: JSON.stringify({ integrationType: IntegrationType.ENVIRONMENT_VARIABLE, name: this.state.name, variables: map }),
            }),
        };
        ServerConnection.makeRequest(
            url,
            init,
            settings
        ).then((response: Response) => {
            Global.handleResponse(response);
            return response.json();
        }).then((body: any) => {
            try {
                var parsed = JSON.parse(body.message)
                // TODO:JJ This is a hacky way to figure out if the returned value is a json data connector (meaning this was successful)
                if (!(parsed.integrationType && parsed.type && parsed.name && parsed.keys)) throw Error()

                this.safeSetState({ waiting: false, addSpinning: false, createSpinning: false })
                if (add && !this.nameHasError(this.state.name)) {
                    const tracker = Global.metadata
                    const optumi = tracker.getMetadata()
                    var integrations = optumi.config.integrations
                    integrations.push(new EnvironmentVariableConfig({
                        name: this.state.name,
                    }))
                    tracker.setMetadata(optumi)
                }
                // Success
                this.handleClose()
            } catch (err) {
                // This means there was a failure
                // Show what went wrong
                this.safeSetState({ waiting: false, addSpinning: false, createSpinning: false, errorMessage: body.message });
            }
        }, (error: ServerConnection.ResponseError) => {
            console.error(error)
            error.response.text().then((text: string) => {
                // Show what went wrong
                this.safeSetState({ waiting: false, addSpinning: false, createSpinning: false, errorMessage: text });
            });
        });
    }

    private handleKeyDown = (event: KeyboardEvent) => {
        if (!this.state.open) return;
        if (event.key === 'Enter') this.handleCreate();
        if (event.key === 'Escape') this.handleClose();
    }

    public render = (): JSX.Element => {
        if (Global.shouldLogOnRender) console.log('CreateEnvironmentVariablePopup (' + new Date().getSeconds() + ')');
        return (
            <DIV sx={Object.assign({}, this.props.sx)}>
                <EnvironmentVariableIdentity
                    description={'Add an environment variable'}
                    handleClick={this.handleClickOpen}
                />
                <StyledDialog
                    open={this.state.open}
                    scroll='paper'
                >
                    <DialogTitle sx={{
                        display: 'inline-flex',
                        height: '60px',
                        padding: '6px',
                    }}>
                        <DIV sx={{
                            display: 'inline-flex',
                            flexGrow: 1,
                            marginLeft: '-6px', // this is to counteract the padding in CreateEnvironmentVariablePopup so we can reuse it without messing with it
                        }}>
                            <EnvironmentVariableIdentity
                                sx={{ zoom: 1.4 }}
                            />
                        </DIV>
                        <DIV>
                            <StyledButton
                                disableElevation
                                sx={{ margin: '6px', height: '36px' }}
                                variant='outlined'
                                onClick={this.handleClose}
                                disabled={this.state.waiting}
                                startIcon={<ArrowBackIos />}
                            >
                                Back
                            </StyledButton>
                        </DIV>
                        <DIV>
                            <Button
                                disableElevation
                                sx={{ margin: '6px', height: '36px' }}
                                variant='contained'
                                color='primary'
                                onClick={() => this.handleCreate(false)}
                                disabled={this.state.waiting}
                            >
                                {this.state.waiting && this.state.createSpinning ? <CircularProgress size='1.75em' /> : 'Create'}
                            </Button>
                            <ExtraInfo reminder='Create and add to your notebook' >
                                <Button
                                    disableElevation
                                    sx={{ margin: '6px', height: '36px' }}
                                    variant='contained'
                                    color='primary'
                                    onClick={() => this.handleCreate(true)}
                                    disabled={(!(Global.labShell.currentWidget instanceof NotebookPanel) && Global.tracker.currentWidget != null) || this.state.waiting}
                                >
                                    {this.state.waiting && this.state.addSpinning ? <CircularProgress size='1.75em' /> : 'Create and add'}
                                </Button>
                            </ExtraInfo>
                        </DIV>
                    </DialogTitle>
                    <ShadowedDivider />
                    <DialogContent sx={{ padding: '0px', display: 'flex' }}>
                        <DIV sx={{ padding: '12px', display: 'flex', flexDirection: 'column' }}>
                            <DIV sx={{ margin: '12px 18px 18px 18px' }}>
                                {"Environment variables are stored encrypted in the Optumi platform and are a convenient way of accessing credentials or configuration options. You can read more about environment variables in python "}
                                <a href='https://docs.python.org/3/library/os.html#os.environ' target='_blank' style={{marginLeft: '3px', color: 'var(--jp-ui-font-color0)', textDecoration: 'underline'}}>
                                    here
                                </a>
                            </DIV>
                            <TextBox<string>
                                getValue={() => this.state.name}
                                saveValue={(value: string) => this.safeSetState({ name: value })}
                                label='Name'
                                helperText='The unique identifier for this environment variable.'
                                labelWidth={EnvironmentVariablePopup.LABEL_WIDTH}
                                disabled={this.state.waiting}
                                required
                            />
                            {this.state.variables.map(variable => (
                                <>
                                    <TextBox<string>
                                        getValue={() => variable.key}
                                        saveValue={(value: string) => {
                                            variable.key = value
                                            if (this.state.variables[this.state.variables.length-1].key != '') {
                                                this.safeSetState({ variables: [...this.state.variables, new EnvironmentVariable()] })
                                            }
                                        }}
                                        label='Variable key'
                                        helperText='The environment variable key.'
                                        labelWidth={EnvironmentVariablePopup.LABEL_WIDTH}
                                        disabled={this.state.waiting}
                                        required
                                    />
                                    <TextBox<string>
                                        getValue={() => variable.value}
                                        saveValue={(value: string) => {
                                            variable.value = value
                                            if (this.state.variables[this.state.variables.length-1].value != '') {
                                                this.safeSetState({ variables: [...this.state.variables, new EnvironmentVariable()] })
                                            }
                                        }}
                                        label='Value'
                                        helperText='The environment variable value.'
                                        labelWidth={EnvironmentVariablePopup.LABEL_WIDTH}
                                        disabled={this.state.waiting}
                                        required
                                    />
                                </>
                            ))}
                            {this.state.errorMessage && (
                                <DIV sx={{
                                    color: Colors.ERROR,
                                    margin: '36px 12px',
                                    wordBreak: 'break-all',
                                    fontSize: '12px',
                                }}>
                                    {this.state.errorMessage}
                                </DIV>
                            )}
                            <DIV sx={{flexGrow: 1}}/>
                            <DIV sx={{
                                margin: '12px 18px',
                                fontStyle: 'italic',
                                fontSize: '14px',
                                textAlign: 'end',
                                // TODO:Beck how do I do this with the theme
                                color: 'gray'
                            }}>
                                *required fields
                            </DIV>
                        </DIV>
                    </DialogContent>
                </StyledDialog>
            </DIV>
        );
    }

    private safeSetState = (map: any) => {
		if (this._isMounted) {
			let update = false
			try {
				for (const key of Object.keys(map)) {
					if (JSON.stringify(map[key]) !== JSON.stringify((this.state as any)[key])) {
						update = true
						break
					}
				}
			} catch (error) {
				update = true
			}
			if (update) {
				if (Global.shouldLogOnSafeSetState) console.log('SafeSetState (' + new Date().getSeconds() + ')');
				this.setState(map)
			} else {
				if (Global.shouldLogOnSafeSetState) console.log('SuppressedSetState (' + new Date().getSeconds() + ')');
			}
		}
	}

    public componentDidMount = () => {
        this._isMounted = true
        document.addEventListener('keydown', this.handleKeyDown, false)
    }

    public componentWillUnmount = () => {
        document.removeEventListener('keydown', this.handleKeyDown, false)
        this._isMounted = false
    }
}