import argparse


def max_one_action(cls):
    """Class decorator to ensure that a command line option appears
    a maximum of one time.  Admittedly, this is contrary to the Unix
    tradition of supporting multiple instances of a given option and
    just using the last one on a command line; however, this developer
    feels that the times when one needs the 'overwrite' capability is
    far less than the time when one would want to flag potentially
    conflicting use."""

    # grab handles to the __init__ and __call__ functions
    class_init = cls.__dict__.get('__init__')  # Possibly None
    class_call = cls.__dict__.get('__call__')  # Possibly None

    def __init__(self, *args, **kwargs):
        # replacement __init__ that notes we have not seen the parameter
        # and then calls either the original __init__ (if it existed) or
        # the next __init__ in the MRO.
        self.seen = False
        if class_init:
            class_init(self, *args, **kwargs)
        else:
            super().__init__(*args, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        # replacement __call__ that checks if we have seen the parameter
        # and, if so, throws ValueError.  Otherwise, it notes that we've
        # been here before and calls either the original __call__ (if it
        # existed) or the next __call__ in the MRO.
        if option_string and self.seen:
            raise ValueError(f'{option_string} supplied more than once')
        self.seen = True
        if class_call:
            class_call(self, parser, namespace, values, option_string)
        else:
            # noinspection PyUnresolvedReferences
            super().__call__(parser, namespace, values, option_string)

    # update the class to use the above function definitions.
    setattr(cls, '__init__', __init__)
    setattr(cls, '__call__', __call__)
    return cls


@max_one_action
class StoreMaxOneAction(argparse.Action):
    # Derived from argparse._StoreAction
    def __init__(
        self,
        option_strings,
        dest,
        nargs=None,
        const=None,
        **kwargs,
    ):
        if nargs == 0:
            raise ValueError(
                'nargs for store actions must be > 0; if you '
                'have nothing to store, actions such as store '
                'true or store const may be more appropriate',
            )
        if const is not None and nargs != argparse.OPTIONAL:
            raise ValueError(
                'nargs must be %r to supply const'
                % argparse.OPTIONAL,
            )
        super().__init__(
            option_strings,
            dest,
            nargs=nargs,
            const=const,
            **kwargs,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


@max_one_action
class StoreConstMaxOneAction(argparse.Action):
    # Derived from argparse._StoreConstAction
    # noinspection PyShadowingBuiltins
    def __init__(
        self,
        option_strings,
        dest,
        const,
        default=None,
        required=False,
        help=None,
        metavar=None,
    ):
        super().__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=0,
            const=const,
            default=default,
            required=required,
            help=help,
            metavar=metavar,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, self.const)


class StoreTrueMaxOneAction(StoreConstMaxOneAction):
    # noinspection PyShadowingBuiltins
    def __init__(
        self,
        option_strings,
        dest,
        default=False,
        required=False,
        help=None,
    ):
        super().__init__(
            option_strings=option_strings,
            dest=dest,
            const=True,
            default=default,
            required=required,
            help=help,
        )
