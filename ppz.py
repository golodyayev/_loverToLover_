import re
import warnings

from telegram import Update
from telegram.ext import Handler
from future.utils import string_types

class MessageHandler2(Handler):

    def __init__(self,
                 filters,
                 callback,
                 allow_edited=False,
                 pass_update_queue=False,
                 pattern=None,
                 pass_job_queue=False,
                 pass_user_data=False,
                 pass_chat_data=False,
                 message_updates=True,
                 channel_post_updates=True,
                 edited_updates=False):
        if not message_updates and not channel_post_updates and not edited_updates:
            raise ValueError(
                'message_updates, channel_post_updates and edited_updates are all False')
        if allow_edited:
            warnings.warn('allow_edited is getting deprecated, please use edited_updates instead')
            edited_updates = allow_edited

        super(MessageHandler2, self).__init__(
            callback,
            pass_update_queue=pass_update_queue,
            pass_job_queue=pass_job_queue,
            pass_user_data=pass_user_data,
            pass_chat_data=pass_chat_data)
        if isinstance(pattern, string_types):
            pattern = re.compile(pattern)
        self.pattern = pattern

        self.filters = filters
        self.message_updates = message_updates
        self.channel_post_updates = channel_post_updates
        self.edited_updates = edited_updates

        # We put this up here instead of with the rest of checking code
        # in check_update since we don't wanna spam a ton
        if isinstance(self.filters, list):
            warnings.warn('Using a list of filters in MessageHandler is getting '
                          'deprecated, please use bitwise operators (& and |) '
                          'instead. More info: https://git.io/vPTbc.')

    def _is_allowed_update(self, update):
        return any([self.message_updates and update.message,
                    self.edited_updates and (update.edited_message or update.edited_channel_post),
                    self.channel_post_updates and update.channel_post])

    def check_update(self, update):
        """Determines whether an update should be passed to this handlers :attr:`callback`.

        Args:
            update (:class:`telegram.Update`): Incoming telegram update.

        Returns:
            :obj:`bool`

        """
        if isinstance(update, Update) and self._is_allowed_update(update):

            if isinstance(update, Update) and update.callback_query:
                if self.pattern:
                    if update.callback_query.data:
                        match = re.match(self.pattern, update.callback_query.data)
                        return bool(match)
                else:
                    return True

                if not self.filters:
                    res = True

                else:
                    message = update.effective_message
                    if isinstance(self.filters, list):
                        res = any(func(message) for func in self.filters)
                    else:
                        res = self.filters(message)
            else:
                return True
        else:
            res = False

        return res

    def handle_update(self, update, dispatcher):
        """Send the update to the :attr:`callback`.

        Args:
            update (:class:`telegram.Update`): Incoming telegram update.
            dispatcher (:class:`telegram.ext.Dispatcher`): Dispatcher that originated the Update.

        """
        if self.pattern:

            optional_args = self.collect_optional_args(dispatcher, update)

            return self.callback(dispatcher.bot, update, **optional_args)
        else:
            True