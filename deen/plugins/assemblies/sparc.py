try:
    import keystone
    import capstone
    KEYSTONE = True
except ImportError:
    KEYSTONE = False

from .__base__ import AsmBase


class DeenPluginAsmSparc(AsmBase):
    name = 'assembly_sparc'
    display_name = 'SPARC'
    aliases = ['asm_sparc',
               'asmsparc',
               'sparc']
    cmd_name = 'assembly_sparc'
    cmd_help='Assemble/Disassemble for the SPARC architecture'
    keystone_arch = keystone.KS_ARCH_SPARC if KEYSTONE else None
    keystone_mode = keystone.KS_MODE_SPARC32 if KEYSTONE else None
    capstone_arch = capstone.CS_ARCH_SPARC if KEYSTONE else None
    capstone_mode = 0 # Add default mode

    @staticmethod
    def add_argparser(argparser, cmd_name, cmd_help, cmd_aliases=None,
                      *args, **kwargs):
        # Add an additional argument for big endian mode.
        parser = AsmBase.add_argparser(argparser, cmd_name,
                                       cmd_help, cmd_aliases=cmd_aliases)
        parser.add_argument('-b', '--big-endian', dest='bigendian',
                            default=False, help='use big endian',
                            action='store_true')
